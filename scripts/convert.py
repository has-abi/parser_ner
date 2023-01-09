__doc__ = """
This module converts assets directory Json training and validation data into 
spacy format stored in corpus directory.
"""
import json
import warnings
from pathlib import Path
from typing import Any, Iterator, List, Tuple, Union

import spacy
import typer
from spacy.tokens import Doc, DocBin

ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"
CORPUS_DIR: Path = Path(__file__).parent.parent / "corpus"


def read_json(file_path: Path) -> Iterator[Tuple[Any, Any]]:
    """Read a Json file as an iterator of text and annotations tuple.

    Args:
        file_path (Path): Json file path.

    Yields:
        Iterator[Tuple[Any, Any]]: Generator of file data
            Tuple of text & annotations.
    """
    with file_path.open(encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for record in json_data:
            yield (record[0], record[1])


def convert_record(
    nlp: Any, text: str, annotations: List[Any], spans_key: str, prob_type: str
) -> Union[Doc, None]:
    """Convert a data recored to spacy format.

    Args:
        nlp (Any): NLP pipline.
        text (str): Record text.
        annotations (List[Any]): Record annotations.
        spans_key (str): The key of spans used in case the problem type is spancat.
        prob_type (str): The problem type to convert the record to.

    Returns:
         Union[Doc, None]: Spacy doc.
    """
    doc = nlp.make_doc(text)
    spans = []
    for annot in annotations:
        span = doc.char_span(annot[0], annot[1], label=annot[2])
        if span is None or span.text.strip() != span.text:
            msg = f"""Skipping entity [{annot[0]}, {annot[1]}, {annot[2]}] in
            the following text because the character span {annot[0]} does not align with token 
            boundaries:\n\n{repr(text)}\n"""
            warnings.warn(msg)
            return None
        spans.append(span)
    if prob_type == "spancat":
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
    convert_type: str = "none",
) -> None:
    """Convert data to spacy format.

    Args:
        assets_dir (Path, optional): Assets data directory path. Defaults to ASSETS_DIR.
        corpus_dir (Path, optional): Corpus data directory path. Defaults to CORPUS_DIR.
        lang (str, optional): Pipline language. Defaults to "fr".
        spans_key (str, optional): Spacy spans key for spancat problem. Defaults to "sc".
        version (int, optional): Data version. Defaults to 1.
        prob_type (str, optional): Problem type (ner, spancat, mixed). Defaults to "spancat".
        convert_type (str, optional): Used to specify if we are going to use the lite version
            of data or use all data when the value is none or different of `lite`.
            Defaults to "none".
    """
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
