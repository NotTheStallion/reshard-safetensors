from safetensors import safe_open
from safetensors.torch import save_file

def merge_safetensor_files(sftsr_files, output_file="model.safetensors"):
    """
    Merge multiple `.safetensors` files into a single file.

    Args:
        sftsr_files (list): List of paths to the `.safetensors` files to merge.
        output_file (str): Path for the output merged file.
    """
    tensors = {}
    for file in sftsr_files:
        with safe_open(file, framework="pt") as sf_tsr:
            metadata = sf_tsr.metadata()
            for layer in sf_tsr.keys():
                blk_tensor = sf_tsr.get_tensor(str(layer))
                tensors[str(layer)] = blk_tensor
    
    save_file(tensors, output_file, metadata)
