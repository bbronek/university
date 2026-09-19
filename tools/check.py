import ast
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    sources = [
        path
        for path in ROOT.glob("semester*/**/*")
        if path.is_file() and not {"build", "bin", "out", ".gradle"} & set(path.parts)
    ]
    python_sources = [path for path in sources if path.suffix == ".py"]
    for path in python_sources:
        ast.parse(path.read_text(), filename=str(path))
    print(f"Parsed {len(python_sources)} Python source files", flush=True)
    for path in sources:
        if path.suffix in {".c", ".cpp"} and "microcontrollers" not in path.parts:
            compiler = "gcc" if path.suffix == ".c" else "g++"
            if shutil.which(compiler):
                subprocess.run(
                    [
                        compiler,
                        "-Wall",
                        "-Wextra",
                        "-Werror",
                        "-fsyntax-only",
                        str(path),
                    ],
                    check=True,
                )
        elif path.suffix == ".rb" or (
            path.name == "run" and "recursive-grammar-parser" in path.parts
        ):
            if shutil.which("ruby"):
                subprocess.run(
                    ["ruby", "-c", str(path)], check=True, stdout=subprocess.DEVNULL
                )
        elif path.name == "run" and "bash" in path.read_text().splitlines()[0]:
            subprocess.run(["bash", "-n", str(path)], check=True)
    for semester in range(1, 8):
        if semester in {1, 3} and not all(
            shutil.which(compiler) for compiler in ("gcc", "g++")
        ):
            print(f"SKIP semester {semester}: install GCC and G++", flush=True)
            continue
        if semester == 5 and not shutil.which("ruby"):
            print("SKIP semester 5: Ruby unavailable", flush=True)
            continue
        if semester == 7 and not all(
            importlib.util.find_spec(name)
            for name in ["numpy", "pandas", "sklearn", "matplotlib"]
        ):
            print(
                "SKIP semester 7: install the scientific Python dependencies",
                flush=True,
            )
            continue
        subprocess.run(
            [sys.executable, str(ROOT / "tests" / f"check_semester{semester}.py")],
            check=True,
        )
    print(
        "Available checks passed. Mbed, R, Haskell, Prolog, Scilab, Thrax, database servers, and neural-network training need their own environments.",
        flush=True,
    )


if __name__ == "__main__":
    main()
