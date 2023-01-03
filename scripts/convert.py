import json
import warnings
from pathlib import Path
from typing import Any, List, Union

import spacy
import typer
from spacy.tokens import Doc, DocBin

ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"
CORPUS_DIR: Path = Path(__file__).parent.parent / "corpus"
NER_ENTITIES = ["SKILL", "PERSON", "ADRESS"]


def read_json(file_path: Path):
    with file_path.open(encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for record in json_data:
            yield (record[0], record[1])


def preprocess_annotations(spans):
    ner_spans = [span for span in spans if span.label_ in NER_ENTITIES]
    spancat_spans = [span for span in spans if span not in ner_spans]
    return (ner_spans, spancat_spans)


def convert_record(
    nlp: Any, text: str, annotations: List[Any], spans_key: str, prob_type: str
) -> Union[Doc, None]:
    doc = nlp.make_doc(text)
    spans = []
    for annot in annotations:
        span = doc.char_span(annot[0], annot[1], label=annot[2])
        if span is None or span.text.strip() != span.text or span.label_ in ["ORG"]:
            msg = f"""Skipping entity [{annot[0]}, {annot[1]}, {annot[2]}] in
            the following text because the character span {annot[0]} does not align with token 
            boundaries:\n\n{repr(text)}\n"""
            warnings.warn(msg)
            return None
        spans.append(span)
    if prob_type == "mixed":
        doc.ents, doc.spans[spans_key] = preprocess_annotations(spans)
    elif prob_type == "spancat":
        doc.spans[spans_key] = spans
    else:
        doc.ents = spans
    return doc


def main(
    assets_dir: Path = ASSETS_DIR,
    corpus_dir: Path = CORPUS_DIR,
    lang: str = "fr",
    spans_key: str = "sc",
    version: int = 1,
    prob_type: str = "spancat",
    convert_type="none",
) -> None:
    nlp = spacy.blank(lang)
    assets_dir = assets_dir / f"v{version}" / "preprocessed"
    for json_file in assets_dir.iterdir():
        if json_file.parts[-1].endswith(".json"):
            docs = [
                convert_record(nlp, text, annotations, spans_key, prob_type)
                for text, annotations in read_json(json_file)
            ]
            docs = [doc for doc in docs if doc]
            if convert_type == "lite":
                docs = docs[: int(len(docs) * 0.3)]
            out_file = (
                corpus_dir / prob_type / json_file.with_suffix(".spacy").parts[-1]
            )
            out_data = DocBin(docs=docs).to_bytes()
            with out_file.open("wb") as data_file:
                data_file.write(out_data)


if __name__ == "__main__":
    typer.run(main)
