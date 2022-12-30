import ast
import csv
import json
import logging
import random
from pathlib import Path

import typer

logger = logging.getLogger()
logger.setLevel(logging.INFO)


ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"


def read_csv(file_path):
    with open(file_path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for idx, row in enumerate(reader):
            if idx > 0:
                yield (row[1], ast.literal_eval(row[2]))


def split_data(data, val_size: float):
    if val_size > 0.5:
        raise ValueError("Validation size must be less than 0.5.")
    train_lenght = int(len(data) * (1 - val_size))
    random_data = random.sample(data, k=len(data))
    return (random_data[:train_lenght], random_data[train_lenght:])


def randomize_data(train_data, val_data):
    return random.sample(train_data, k=len(train_data)), random.sample(
        val_data, k=len(val_data)
    )


def save_data(file_dist, data):
    with open(file_dist, "w", encoding="utf-8") as file_to_save:
        json.dump(data, file_to_save, ensure_ascii=False)


def preprocess(version: int = 1, val_size: float = 0.2):
    RAW_DATA = ASSETS_DIR / f"v{version}" / "raw"
    OUTPUT = ASSETS_DIR / f"v{version}" / "preprocessed"
    train_data = []
    val_data = []
    for file_data in RAW_DATA.iterdir():
        logging.info("Preprocessing %s ...", file_data.parts[-1])
        file_train_data, file_val_data = split_data(
            list(read_csv(file_data))[1:], val_size
        )
        train_data += file_train_data
        val_data += file_val_data
    train_data, val_data = randomize_data(train_data, val_data)

    logging.info("Size of the training data: %s", len(train_data))
    logging.info("Size of the validation data: %s", len(val_data))

    save_data(OUTPUT / "train.json", train_data)
    save_data(OUTPUT / "val.json", val_data)


if __name__ == "__main__":
    typer.run(preprocess)
