

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
├── README.md
├── requirements.txt
```


# Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NotTheStallion/reshard-safetensors
    cd reshard-safetensors/
    ```

2. Install the required dependencies:

    ```bash
    # use python, python3 or whatever applies to you
    python -m pip install -r requirements.txt
    ```

3. Setup:

    ```bash
    python setup.py
    ```

# Usage

## Merging Safetensors Files

To merge all `.safetensors` files in a directory:
- Modify the folder/location string in `scripts/merge_files.py` to match your chosen directory.

## Splitting a Safetensor File

To split a .safetensors file into a specified number of chunks:
- Modify the `scripts/split_file.py` script to match your desired safetensor file name and the desired number of shards/chunks to split into 

# License

This project is licensed under the MIT License.
