__doc__ = """
This module is used to plot different statistiques about raw
and training data in terminal using plotext package.
"""
import logging
from collections import Counter
from pathlib import Path
from typing import Any, List, Tuple

import plotext as plt
import typer

from scripts.convert import read_json
from scripts.preprocess import read_csv

logger = logging.getLogger()
logger.setLevel(logging.INFO)


ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"


def plot_entities(file_name: str, data: List[Tuple[Any, Any]]) -> None:
    """Plot the summary of entities founed in `data`.

    Args:
        file_name (str): File data.
        data (List[Tuple[Any, Any]]): Data entities to plot.
    """
    annotations = [label for _, annotations in data for _, _, label in annotations]
    annot_counter = Counter(annotations)
    entities = list(annot_counter.keys())
    entities_count = list(annot_counter.values())
    plt.simple_bar(
        entities,
        entities_count,
        title=f"Distibution of the entities found in {file_name}",
        width=100,
    )
    plt.show()


def get_data_entities_summary(
    train_entities: List[str], val_entities: List[str]
) -> Tuple[List[str], List[int], List[int]]:
    """Get the summary of training and validation data entities.

    Args:
        train_entities (List[str]): Train data entities.
        val_entities (List[str]): Validation data entities.

    Returns:
        Tuple[List[str], List[int], List[int]]: All entities and their count
            in the train and validation entities.
    """
    train_counter = Counter(train_entities)
    val_counter = Counter(val_entities)
    entities = list(train_counter.keys())
    train_entities_count = list(train_counter.values())
    val_entities_count = [val_counter[entity] for entity in entities]
    return entities, train_entities_count, val_entities_count


def plot_preprocessed_stats(
    train_data: List[Tuple[Any, Any]], val_data: List[Tuple[Any, Any]]
) -> None:
    """Plot the training and validation data entities stats.

    Args:
        train_data (List[Tuple[Any, Any]]): Training data.
        val_data (List[Tuple[Any, Any]]): Validation data.
    """
    train_entities = [
        annot[2] for _, annotations in train_data for annot in annotations
    ]
    val_entities = [label for _, annotations in val_data for _, _, label in annotations]
    plt.simple_bar(
        ["TRAIN", "VALIDATION"],
        [len(train_entities), len(val_entities)],
        title="Distibution of labeled entities in the training & the validation data",
        width=100,
    )
    plt.show()

    entities, train_entities_count, val_entities_count = get_data_entities_summary(
        train_entities, val_entities
    )
    plt.simple_multiple_bar(
        entities,
        [train_entities_count, val_entities_count],
        labels=["train", "validation"],
        title="Trainig and validation entities summary.",
        width=100,
    )
    plt.show()


def show_stats(version: int = 1, data_type: str = "raw"):
    """Show raw data or train/validation data based on
    `data_type` and `version`.

    Args:
        version (int, optional): Data version. Defaults to 1.
        data_type (str, optional): Data type to show stats for. Defaults to "raw".
    """
    if data_type == "raw":
        raw_path = ASSETS_DIR / f"v{version}" / "raw"
        raw_data = {}
        for file_data in raw_path.iterdir():
            file_name = file_data.parts[-1]
            raw_data[file_name] = list(read_csv(file_data))[1:]

        for file_name, data in raw_data.items():
            plot_entities(file_name, data)

    elif data_type == "training":
        preprocessed_path = ASSETS_DIR / f"v{version}" / "preprocessed"

        train_data = read_json(preprocessed_path / "train.json")
        val_data = read_json(preprocessed_path / "val.json")

        plot_preprocessed_stats(list(train_data), list(val_data))
    else:
        logging.info(
            "To see the data summary visualisations use data_type=raw or data_type=training"
        )


if __name__ == "__main__":
    typer.run(show_stats)
