import os

import pathlib

directory_str = pathlib.Path().absolute()
directory = os.fsencode(directory_str)

def rename(path1, path2, i):
    try:
        os.rename(path1, path2 if i == 0 else f"{path2}({i})")
    except:
        return

for direct in os.listdir(directory):
    direct_name = os.fsdecode(direct)
    if direct_name.endswith(".py") or direct_name.endswith(".md") or direct_name.endswith(".json"):
        continue

    inner_directory_str = f"{directory_str}\\{direct_name}"
    inner_directory = os.fsencode(inner_directory_str)
    for file in os.listdir(inner_directory):
        filename = os.fsdecode(file)
        if not filename.endswith(".json"):
            continue
        
        rename(f"{inner_directory_str}\\{filename}", f"{directory_str}\\{filename}", 0)

