from .file_utils import get_safetensor_files
from .merger import merge_safetensor_files
from .splitter import split_safetensor_file
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="SafeTensors management tool")
    parser.add_argument("--type", choices=["merge", "split"], required=True, help="Operation type")
    parser.add_argument("--num_shards", type=int, help="Number of shards for splitting")
    parser.add_argument("--input", required=True, help="Input file/dir path")
    parser.add_argument("--output", required=True, help="Output file/dir path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    args = parser.parse_args()
    
    if args.type == "merge":
        if args.num_shards is not None:
            print("Warning: num_shards argument is ignored for merge operation.")
        
        # @note : To merge multiple files, a directory must be provided as input
        if not os.path.isdir(args.input):
            print("Error: For merge operation, input must be a directory containing safetensor files.")
            return
        
        # Get all safetensor files from the input directory
        sftsr_files = get_safetensor_files(args.input)
        if args.verbose:
            print(f"Merging the following files: {sftsr_files}")
    
        merge_safetensor_files(sftsr_files, args.output)
    
    
    elif args.type == "split":
        if not args.num_shards:
            print("Error: num_shards argument is required for split operation.")
            return
        
        split_safetensor_file(args.input, args.output, args.num_shards, verbose=args.verbose)

if __name__ == "__main__":
    main()