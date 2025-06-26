import subprocess
import time
import os
import re

EXCLUDED_DIRS = [
    ".git",
]

with open(".gitignore", "r", encoding="utf8") as f:
    for line in f.readlines():
        line = line.strip()

        if line:
            if line[0] != "#" and line[-1] == "/":
                EXCLUDED_DIRS.append(line)


def scan_recursive(pattern: str, directory: str = "."):
    folders = [directory]
    matches = []

    while folders:
        folder = folders.pop(0)
        folder_content = os.listdir(folder)
        for item in folder_content:
            if item not in EXCLUDED_DIRS:
                item = os.path.join(folder, item)
                if re.match(pattern, item):
                    matches.append(os.path.abspath(item))

                if os.path.isdir(item):
                    folders.append(os.path.abspath(item))

    return matches


def lint():
    html_files = scan_recursive(r"^.*\.html$")
    for file in html_files:
        subprocess.run(["djhtml", file])


def lint_watch():
    try:
        rescan_counter = 0
        html_files = scan_recursive(r"^.*\.html$")
        timestamps = {}
        while True:
            if rescan_counter == 30:
                html_files = scan_recursive(r"^.*\.html$")
                rescan_counter = 0

            for file in html_files:
                try:
                    last_modified = os.stat(file).st_mtime_ns
                    try:
                        if timestamps[file] < last_modified:
                            print(file, "modified")
                            subprocess.run(["djhtml", file])
                            timestamps[file] = os.stat(file).st_mtime_ns + 1

                    except KeyError:
                        timestamps.update({file: last_modified})

                except FileNotFoundError:
                    html_files = scan_recursive(r"^.*\.html$")
                    rescan_counter = 0

            rescan_counter += 1
            time.sleep(1 / 10)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    import sys

    try:
        if sys.argv[1] == "--watch":
            print("Waiting for changes in '.html' files...")
            lint_watch()
        else:
            lint()

    except IndexError:
        lint()
