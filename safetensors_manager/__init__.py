# This file makes the `safetensors_manager` directory a package.
"""
SafeTensors Manager Package
A command-line tool for managing SafeTensors files with merge and split operations.
Usage:
    python -m safetensors_manager --type merge --input <input_path> --output <output_path>
    python -m safetensors_manager --type split --input <input_path> --output <output_path> --num_shards <number>
Arguments:
    --type (str): Operation type - either 'merge' or 'split' (required)
    --input (str): Path to input file or directory (required)
    --output (str): Path to output file or directory (required)
    --num_shards (int): Number of shards for split operation (required for split, optional for merge)
Example:
    # Merge multiple safetensor files
    python -m safetensors_manager --type merge --input ./shards/ --output ./merged_model.safetensors
    # Split a safetensor file into 4 shards
    python -m safetensors_manager --type split --input ./model.safetensors --output ./shards/ --num_shards 4
Available Functions:
    - get_safetensor_files(): Retrieve SafeTensor files from a directory
    - merge_safetensor_files(): Merge multiple SafeTensor files into one
    - split_safetensor_file(): Split a SafeTensor file into multiple shards
Version: 1.0.1
"""

# Optional: Import specific modules to make them accessible directly from the package.
from .file_utils import get_safetensor_files
from .merger import merge_safetensor_files
from .splitter import split_safetensor_file
import argparse

# Define the package version if needed
__version__ = "1.0.1"
