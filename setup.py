import os
import pathlib
import fnmatch
import sys

"""
Run this script once after first creating the repository from the template.

This script is interactive and will prompt you for various inputs.
"""

if __name__ == "__main__":
    repo_name = input("What is the name of your plugin (full name with spaces)? ")

    snake_name = "_".join(repo_name.lower().split(" "))

    os.rename("my_plugin.py", f"{snake_name}.py")

    for file in pathlib.Path(".").glob("**/*.*"):
        filename = str(file)

        if fnmatch.fnmatch(filename, ".git/*"):  # Exclude .git directory
            continue

        if fnmatch.fnmatch(filename, "__pycache__/*"):  # Exclude __pycache__ directory
            continue

        if fnmatch.fnmatch(filename, ".idea*"):
            continue

        if fnmatch.fnmatch(filename, sys.argv[0]):  # Exclude the script file itself
            continue

        if os.path.basename(file) == "setup.py":
            continue

        if file.is_dir():
            continue
        else:
            print(file)
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            replaced = content.replace("my_plugin", snake_name).replace("My plugin", repo_name.title())

            with open(file, "w", encoding="utf-8", errors="ignore") as f:
                f.write(replaced)

    print(f"All the occurrences were replaced successfully with `{repo_name}`!")
    os.remove(sys.argv[0])
