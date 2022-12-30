import json
import warnings
from pathlib import Path
from typing import Any, List

import spacy
import typer
from spacy.tokens import Doc, DocBin

ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"
CORPUS_DIR: Path = Path(__file__).parent.parent / "corpus"


def read_json(file_path: Path):
    with file_path.open(encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for record in json_data:
            yield (record[0], record[1])


def convert_record(nlp: Any, text: str, annotations: List[Any], spans_key: str) -> Doc:
    doc = nlp.make_doc(text)
    spans = []
    for annot in annotations:
        span = doc.char_span(annot[0], annot[1], label=annot[2])
        if span is None:
            msg = f"""Skipping entity [{annot[0]}, {annot[1]}, {annot[2]}] in
            the following text because the character span {annot[0]} does not align with token 
            boundaries:\n\n{repr(text)}\n"""
            warnings.warn(msg)
        else:
            spans.append(span)
    doc.spans[spans_key] = spans
    return doc


def main(
    assets_dir: Path = ASSETS_DIR,
    corpus_dir: Path = CORPUS_DIR,
    lang: str = "fr",
    spans_key: str = "sc",
    version: int = 1,
) -> None:
    nlp = spacy.blank(lang)
    assets_dir = assets_dir / f"v{version}" / "preprocessed"
    for json_file in assets_dir.iterdir():
        if json_file.parts[-1].endswith(".json"):
            docs = [
                convert_record(nlp, text, annotations, spans_key)
                for text, annotations in read_json(json_file)
            ]
            out_file = corpus_dir / json_file.with_suffix(".spacy").parts[-1]
            out_data = DocBin(docs=docs).to_bytes()
            with out_file.open("wb") as data_file:
                data_file.write(out_data)


if __name__ == "__main__":
    typer.run(main)
