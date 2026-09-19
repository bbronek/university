from pathlib import Path
import os
import runpy
import shutil
import sqlite3
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SEMESTER = ROOT / "semester2"


def main():
    rref = runpy.run_path(str(SEMESTER / "linear-algebra/rref.py"))["rref"]
    matrix = [[0, 2, 4], [1, 3, 5]]
    assert rref(matrix) == [[1, 0, -1], [0, 1, 2]]
    assert matrix == [[0, 2, 4], [1, 3, 5]]
    assert rref([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]
    assert rref([]) == []
    cycles = runpy.run_path(str(SEMESTER / "linear-algebra/lab1/permutations2.py"))[
        "cycles"
    ]
    assert cycles([1, 2, 3]) == []
    assert cycles([2, 3, 1]) == [[1, 2, 3]]
    schema = (SEMESTER / "databases/conceptual-project/schema.sql").read_text()
    schema = "\n".join(
        line for line in schema.splitlines() if line.strip().lower() != "go"
    )
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(schema)
    assert connection.execute("SELECT count(*) FROM Vehicle").fetchone()[0] == 2
    assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
    connection.close()

    javac = shutil.which("javac")
    java = shutil.which("java")
    if not javac or not java:
        print("SKIP Java checks: install a JDK and add it to PATH")
    else:
        groups = [
            "oop/examples/lesson1",
            "oop/examples/lesson2/src",
            "oop/examples/lesson3/src",
            "oop/lab1/src",
            "oop/lab2/src",
            "oop/lab3/src",
            "oop/pesel/src/main/java",
            "oop/students/src",
            "databases/db-connection/java_conn",
        ]
        with tempfile.TemporaryDirectory() as temporary:
            for index, group in enumerate(groups):
                output = Path(temporary) / str(index)
                output.mkdir()
                sources = list((SEMESTER / group).rglob("*.java"))
                subprocess.run(
                    [javac, "-d", str(output), *map(str, sources)],
                    check=True,
                    timeout=30,
                )
                if group == "oop/pesel/src/main/java":
                    destination = output / "inhabitants.txt"
                    result = subprocess.run(
                        [java, "-cp", str(output), "App", str(destination)],
                        input="Warsaw\nJohn Doe 02070803628\ny\nLondon\nJane Doe 02070803628\ny\nParis\nBad Input 123\nn\n",
                        capture_output=True,
                        text=True,
                        check=True,
                        timeout=10,
                    )
                    assert (
                        destination.read_text().strip() == "London Jane Doe 02070803628"
                    ), result
                if group == "oop/students/src":
                    destination = output / "students.txt"
                    subprocess.run(
                        [java, "-cp", str(output), "MainStudent", str(destination)],
                        input="f123\nJohn\nDoe\nn\n",
                        capture_output=True,
                        text=True,
                        check=True,
                        timeout=10,
                    )
                    assert destination.read_text().strip() == "John Doe f123"
    print("Semester 2 checks passed")


if __name__ == "__main__":
    main()
