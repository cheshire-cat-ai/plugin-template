"""
Run this script once after first creating the repository from the template.

This script is interactive and will prompt you for various inputs.
"""

import os
import pathlib
import fnmatch
from sys import argv


if __name__ == "__main__":
    repo_name = input("What is the name of your plugin (full name with spaces) ? ")

    snake_name = ("_").join(repo_name.lower().split(" "))

    os.rename("my_plugin.py", snake_name)
    
    for file in pathlib.Path(".").glob('**/*.*'):
        filename = str(file)
        
        if fnmatch.fnmatch(filename, ".git") or fnmatch.fnmatch(filename, ".git\*"):
            continue
        
        if os.path.basename(file) == "setup.py":
            continue
        
        if file.is_dir():
            continue
        else:
            with open(file, "r") as f:
                content = f.read()

            replaced = content.replace("my_plugin", snake_name).replace("My plugin", repo_name.title())

            with open(file, "w") as f:
                f.write(replaced)
    
    print(f"All the occurrencies were replaced successfully with `{repo_name}` !")
    os.remove(argv[0])
