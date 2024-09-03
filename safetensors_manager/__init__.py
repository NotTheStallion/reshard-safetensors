# This file makes the `safetensors_manager` directory a package.

# Optional: Import specific modules to make them accessible directly from the package.
from .file_utils import get_safetensor_files
from .merger import merge_safetensor_files
from .splitter import split_safetensor_file

# Define the package version if needed
__version__ = "1.0.0"
