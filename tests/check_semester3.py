from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
import shutil
import socket
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SEMESTER = ROOT / "semester3"


def main():
    graph = runpy.run_path(str(SEMESTER / "discrete-mathematics/qaszel_airways.py"))[
        "Graph"
    ]()
    graph.add_edge(1, 2)
    graph.add_edge(1, 2)
    graph.remove_edge(1, 2)
    assert graph.vertices[1].neighbours == []
    assert graph.vertices[2].neighbours == []
    client = runpy.run_path(str(SEMESTER / "computer-networks/lab5/tic-tac-toe.py"))
    assert client["find_move"]([True, False]) == 1
    assert client["find_move"]([True] * 25) is None
    with tempfile.TemporaryDirectory() as temporary:
        for index, source in enumerate(SEMESTER.rglob("*.cpp")):
            subprocess.run(
                [
                    "g++",
                    "-Wall",
                    "-Wextra",
                    "-Werror",
                    str(source),
                    "-o",
                    str(Path(temporary) / str(index)),
                ],
                check=True,
            )
        if not shutil.which("javac"):
            print("SKIP game integration: install a JDK")
            return
        source = SEMESTER / "computer-networks/lab5/TicTacToeServer.java"
        subprocess.run(["javac", "-d", temporary, str(source)], check=True)
        server = subprocess.Popen(
            ["java", "-cp", temporary, "TicTacToeServer", "0"],
            cwd=temporary,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            port = int(server.stdout.readline().split()[-1])
            with socket.create_connection(("127.0.0.1", port), timeout=5) as connection:
                responses = connection.makefile("r")
                assert responses.readline().startswith("WELCOME")
                connection.sendall(b"LOGIN Tester\nMOVE -1\nMOVE 0\n")
                assert responses.readline().strip() == "OK"
                assert responses.readline().strip() == "YOUR_TURN"
                assert responses.readline().strip() == "ERROR"
                assert responses.readline().strip() == "OK"
                assert responses.readline().startswith("OPPONENT ")
                assert responses.readline().strip() == "YOUR_TURN"
                responses.close()
            with redirect_stdout(io.StringIO()):
                assert client["play"]("127.0.0.1", port, "Regression") in {
                    "SUCCESS",
                    "FAILED",
                }
        finally:
            server.terminate()
            server.communicate(timeout=5)
    print("Semester 3 checks passed")


if __name__ == "__main__":
    main()
