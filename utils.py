import os

def find_filenames_by_ext(path_to_dir: str, ext: str=".csv" ):
    return [ os.path.join(path_to_dir, filename) for filename in os.listdir(path_to_dir) if filename.endswith(ext)]