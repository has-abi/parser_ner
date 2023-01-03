__doc__ = """
This module is used to preprocess raw CSV annotations and convert them to
two Json file train.json for train data and val.json for validation data. 
"""
import ast
import csv
import json
import logging
import random
from pathlib import Path
from typing import Any, Iterator, List, Tuple

import typer

logger = logging.getLogger()
logger.setLevel(logging.INFO)


ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"


def read_csv(file_path: Path) -> Iterator[Tuple[Any, Any]]:
    """Read a CSV file as an iterator of text and annotations tuple.

    Args:
        file_path (Path): CSV file path.

    Yields:
        Iterator[Tuple[Any, Any]]: Generator of file data
            Tuple of text & annotations.
    """
    with open(file_path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for idx, row in enumerate(reader):
            if idx > 0:
                yield (row[1], ast.literal_eval(row[2]))


def split_data(data: List[Any], val_size: float) -> Tuple[List[Any], List[Any]]:
    """Split data to train and validation sets based on the value of
    `val_size`.

    Args:
        data (List[Any]): Data to split.
        val_size (float): The validation data size.

    Raises:
        ValueError: Thrown if the value of `val_size` is greater than 0.5

    Returns:
        Tuple[List[Any], List[Any]]: Train and validation sets.
    """
    if val_size > 0.5:
        raise ValueError("Validation size must be less than 0.5.")
    train_lenght = int(len(data) * (1 - val_size))
    random_data = random.sample(data, k=len(data))
    return (random_data[:train_lenght], random_data[train_lenght:])


def randomize_data(
    train_data: List[Any], val_data: List[Any]
) -> Tuple[List[Any], List[Any]]:
    """Randomize the training and validation sets using
    sample function of random module.

    Args:
        train_data (List[Any]): Training data.
        val_data (List[Any]): Validation data.

    Returns:
        Tuple[List[Any], List[Any]]: Train and validation data
            randomized.
    """
    return random.sample(train_data, k=len(train_data)), random.sample(
        val_data, k=len(val_data)
    )


def save_data(file_dist: Path, data: Any):
    """Save `data` of to `file_dist`.

    Args:
        file_dist (Path): File distination path.
        data (Any): Data to save.
    """
    with open(file_dist, "w", encoding="utf-8") as file_to_save:
        json.dump(data, file_to_save, ensure_ascii=False)


def preprocess(version: int = 1, val_size: float = 0.2):
    """Main function that processes assets/raw directory data based
    on `version` and `val_size` and save the training and validation
    data to assets/prepocessed directory.

    Args:
        version (int, optional): Raw data version. Defaults to 1.
        val_size (float, optional): Validation set size. Defaults to 0.2.
    """
    raw_data = ASSETS_DIR / f"v{version}" / "raw"
    output = ASSETS_DIR / f"v{version}" / "preprocessed"
    train_data = []
    val_data = []
    for file_data in raw_data.iterdir():
        logging.info("Preprocessing %s ...", file_data.parts[-1])
        file_train_data, file_val_data = split_data(
            list(read_csv(file_data))[1:], val_size
        )
        train_data += file_train_data
        val_data += file_val_data
    train_data, val_data = randomize_data(train_data, val_data)

    logging.info("Size of the training data: %s", len(train_data))
    logging.info("Size of the validation data: %s", len(val_data))

    save_data(output / "train.json", train_data)
    save_data(output / "val.json", val_data)


if __name__ == "__main__":
    typer.run(preprocess)
