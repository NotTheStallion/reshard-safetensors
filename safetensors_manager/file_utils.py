import os

def get_safetensor_files(directory):
    """
    Retrieve all `.safetensors` files within a directory.

    Args:
        directory (str): The directory path to search.

    Returns:
        list: A list of paths to the found `.safetensors` files.
    """
    safetensors_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".safetensors"):
                safetensors_files.append(os.path.join(root, file))
    return safetensors_files
