

# Safetensors Manager

## Overview

Safetensors Manager is a Python package designed to handle the merging and splitting of `.safetensors` files. It allows you to combine multiple `.safetensors` files into one or split a large `.safetensors` file into smaller chunks/shards for easier management while also generating the `model.safetensors.index.json` and `chunk_paths.json` files ( HuggingFace standards ).


## Project Structure

```plaintext
safetensors_manager/
├── safetensors_manager/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── merger.py
│   ├── splitter.py
├── scripts/
│   ├── merge_files.py
│   ├── split_file.py
├── tests/
│   ├── test_file_utils.py
│   ├── test_merger.py
│   ├── test_splitter.py
├── README.md
├── requirements.txt
```


# Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd scripts
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Setup:

    ```bash
    python setup.py
    ```

# Usage

## Merging Safetensors Files

To merge all `.safetensors` files in a directory:
- Modify the directory in `scripts/merge_files.py` to your directory.

## Splitting a Safetensor File

To split a .safetensors file into a specified number of chunks:
- Modify the safetensor file and the number of shards/chunks in `scripts/split_file.py`

# License

This project is licensed under the MIT License.