import subprocess
import time
import sys


def dev():
    try:
        p1 = subprocess.Popen(["uv", "run", "manage.py", "runserver"])
    except FileNotFoundError:
        p1 = subprocess.Popen(["uv", "run", "manage.py", "runserver"], shell=True)

    try:
        p2 = subprocess.Popen(["npm", "run", "dev"])
    except FileNotFoundError:
        p2 = subprocess.Popen(["npm", "run", "dev"], shell=True)
    try:
        while True:
            time.sleep(999)
    except KeyboardInterrupt:
        p1.kill()
        p2.kill()


if __name__ == "__main__":
    try:
        script = sys.argv[1]
    except IndexError:
        exit("Usage: scripts.py <script>")

    match script:
        case "dev":
            dev()

        case _:
            exit(f"Script not found: '{script}'")
