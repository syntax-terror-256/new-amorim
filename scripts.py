import subprocess
import time
import sys


def dev(address: str):
    try:
        p1 = subprocess.Popen(["uv", "run", "manage.py", "runserver", address])
    except FileNotFoundError:
        p1 = subprocess.Popen(
            ["uv", "run", "manage.py", "runserver", address],
            shell=True,
        )

    try:
        p2 = subprocess.Popen(["npm", "run", "dev"])
    except FileNotFoundError:
        p2 = subprocess.Popen(["npm", "run", "dev"], shell=True)

    try:
        p3 = subprocess.Popen(["uv", "run", "lint.py", "--watch"])
    except FileNotFoundError:
        p3 = subprocess.Popen(["uv", "run", "lint.py", "--watch"], shell=True)

    try:
        while True:
            time.sleep(999)
    except KeyboardInterrupt:
        p1.kill()
        p2.kill()
        p3.kill()


if __name__ == "__main__":
    try:
        script = sys.argv[1]
    except IndexError:
        exit("Usage: scripts.py <script>")

    match script:
        case "dev":
            addres = ""
            if len(sys.argv) >= 3:
                addres = sys.argv[2]
            dev(addres)

        case _:
            exit(f"Script not found: '{script}'")
