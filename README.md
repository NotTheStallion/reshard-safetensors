

# Safetensors Manager

## Overview

Safetensors Manager is a Python package designed to handle the merging and splitting of `.safetensors` files. It allows you to combine multiple `.safetensors` files into one or split a large `.safetensors` file into smaller chunks/shards for easier management while also generating the `model.safetensors.index.json` and `chunk_paths.json` files ( HuggingFace standards ).


# Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NotTheStallion/reshard-safetensors
    cd reshard-safetensors/
    python -m pip install -r requirements.txt
    ```


# Usage

## Merging Safetensors Files

Put all the `.safetensors` files you want to merge into a single directory `safetensor_dir`. Then, run :
```bash
    python -m safetensors_manager --type merge --input safetensor_dir --output merged_model.safetensors --verbose
```

## Splitting a Safetensor File

To split a large `.safetensors` file into smaller chunks/shards and put them in a directory `safetensor_dir`, run:
```bash
    python -m safetensors_manager --type split --num_shards 8 --input big_model.safetensors --output safetensor_dir --verbose
```

# License

This project is licensed under the MIT License.
