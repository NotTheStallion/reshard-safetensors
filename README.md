

# Safetensors Manager

## Overview

Safetensors Manager is a Python package designed to handle the merging and splitting of `.safetensors` files. It allows you to combine multiple `.safetensors` files into one or split a large `.safetensors` file into smaller chunks/shards for easier management.


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
    cd safetensors_manager
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

# Usage

## Merging Safetensors Files

To merge all `.safetensors` files in a directory:

```bash
python scripts/merge_files.py /path/to/directory
```

## Splitting a Safetensor File

To split a .safetensors file into a specified number of chunks:

```bash
python scripts/split_file.py /path/to/file.safetensors <number_of_chunks>
```

# License

This project is licensed under the MIT License.