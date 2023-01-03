<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Entities extraction from resume sections (NER/SpanCat).

This project uses spaCy (NER) / (Span Categorizer) to extract resume entities

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Preprocess different sections data and merge it in two training and validation files |
| `show-stats-raw` | Show different stats about raw data |
| `show-stats-training` | Show different stats about training data |
| `convert` | Convert data to spaCy format |
| `debug` | debug training data |
| `train` | Train spaCy pipline |
| `evaluate` | Evaluate the trained model and export metrics |
| `clean-preprocessed` | Delete the preprocessed files |
| `clean` | Clean corpus and training data files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `show-stats-training` &rarr; `convert` &rarr; `train` &rarr; `evaluate` |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

### Train data summary
![Alt text](training_data_stats.PNG "Training data summary...")