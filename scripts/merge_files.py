import sys
from safetensors_manager.file_utils import get_safetensor_files
from safetensors_manager.merger import merge_safetensor_files

if __name__ == "__main__":
    safetensor_files = get_safetensor_files("./scripts/shards")
    print(f"The fllowing shards/chunks will be merged : {safetensor_files}")
    
    merge_safetensor_files(safetensor_files, output_file="model.safetensors")
    
    
