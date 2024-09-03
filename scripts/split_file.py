from safetensors_manager.file_utils import get_safetensor_files
from safetensors_manager.splitter import split_safetensor_file

if __name__=="__main__":
    safetensor_file = "scripts/global/model.safetensors"
    split_safetensor_file(safetensor_file, 7, verbose=True)