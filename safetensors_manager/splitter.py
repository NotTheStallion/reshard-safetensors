import os
import math
import json
from safetensors import safe_open
from safetensors.torch import save_file

def guess_layer_size(shape, dtype):
    """
    Guess the size of a tensor layer based on its shape and data type.

    Args:
        shape (list): The shape of the tensor.
        dtype (str): The data type of the tensor.

    Returns:
        int: The calculated size of the tensor layer in bytes.
    """
    if not isinstance(shape, list):
        raise ValueError("Not a valid shape format.")
    
    size = 1
    for dim in shape:
        if dim is not None:
            size *= dim

    if dtype == 'F32':
        size *= 4
    else:
        raise ValueError("Data type not supported")

    return size



def split_safetensor_file(filepath, num_chunks=1, verbose=False):
    """
    Split a `.safetensors` file into multiple chunks.

    Args:
        filepath (str): The path to the `.safetensors` file to split.
        num_chunks (int): Number of chunks to split the file into.

    Returns:
        None
    """
    basename = os.path.basename(filepath)
    dirname = os.path.dirname(filepath)
    extension = basename.split(".")[-1]
    
    filename_no_ext = basename.split(".")[-2] 
    file_size = os.path.getsize(filepath)
    chunk_size = file_size // num_chunks
    if verbose : print(f"Size Logic : {file_size} = {num_chunks} x {chunk_size}\n\n")

    digit_count = 5
    chunk_paths = []
    model_index = {"metadata":{"total_size":file_size}, "weight_map":{}}
    chunk_tensors = {}
    cumul_size_sum = 0
    chunk_id = 1

    with safe_open(filepath, framework="pt") as sf_tsr:
        metadata = sf_tsr.metadata()
        for layer in sf_tsr.keys():
            blk_shape = sf_tsr.get_slice(str(layer)).get_shape()
            blk_type = sf_tsr.get_slice(str(layer)).get_dtype()
            blk_tensor = sf_tsr.get_tensor(str(layer))
            
            cumul_size_sum += guess_layer_size(blk_shape, blk_type)
            
            if cumul_size_sum > chunk_size - 8:
                if verbose : print(f"\nGoal :", chunk_size,"reached",cumul_size_sum-guess_layer_size(blk_shape, blk_type))
                
                chunk_filename = f"{filename_no_ext}-{str(chunk_id).zfill(digit_count)}-of-{str(num_chunks).zfill(digit_count)}.{extension}"
                split_path = os.path.join(dirname, chunk_filename)
                save_file(chunk_tensors, split_path, metadata)
                if verbose : print(f"save {split_path}\n\n")
                
                chunk_paths.append(chunk_filename)
                
                chunk_id += 1
                cumul_size_sum = 0
                chunk_tensors = {}
            
            chunk_tensors[str(layer)] = blk_tensor
            if verbose : print("|_|",end="")
            model_index["weight_map"][layer] = f"{filename_no_ext}-{str(chunk_id).zfill(digit_count)}-of-{str(num_chunks).zfill(digit_count)}.{extension}"

        if verbose : print(f"\nGoal :", chunk_size,"reached",cumul_size_sum-guess_layer_size(blk_shape, blk_type))
        chunk_filename = f"{filename_no_ext}-{str(chunk_id).zfill(digit_count)}-of-{str(num_chunks).zfill(digit_count)}.{extension}"
        split_path = os.path.join(dirname, chunk_filename)
        chunk_paths.append(chunk_filename)
        save_file(chunk_tensors, split_path, metadata)
        if verbose : print(f"save {split_path}\n\n")
    
    with open("chunk_paths.json", 'w') as f:
        json.dump(chunk_paths, f)
    
    with open("model.safetensors.index.json", 'w') as f:
        json.dump(model_index, f)
