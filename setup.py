import os
import pathlib
import fnmatch
import sys

"""
Run this script once after first creating the repository from the template.

This script is interactive and will prompt you for various inputs.
"""


def filter_lines(file_path, excluded_ranges):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    current_line = 1
    for line in lines:
        exclude = any(start <= current_line <= end for start, end in excluded_ranges)
        if not exclude:
            new_lines.append(line)
        current_line += 1

    with open(file_path, 'w') as file:
        file.writelines(new_lines)


if __name__ == "__main__":

    repo_name = input("What is the name of your plugin (full name with spaces)? ")

    snake_name = "_".join(repo_name.lower().split(" "))

    os.rename("my_plugin.py", f"{snake_name}.py")

    # Pipeline file's line ranges to remove
    # This must reflect eventual main.yml changes
    excluded_line_ranges = [(24, 35), (37, 40)]

    yaml_file_path = os.path.join(os.path.dirname(__file__), '.github', 'workflows', 'main.yml')

    filter_lines(yaml_file_path, excluded_line_ranges)

    for file in pathlib.Path(".").glob("**/*.*"):
        filename = str(file)

        if fnmatch.fnmatch(filename, ".git/*"):  # Exclude .git directory
            continue

        if fnmatch.fnmatch(filename, "__pycache__/*"):  # Exclude __pycache__ directory
            continue

        if fnmatch.fnmatch(filename, "venv/*"):  # Exclude venv directory
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
