from pathlib import Path
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FORMAL = ROOT / "semester5/formal-languages"


def main():
    automaton = runpy.run_path(str(FORMAL / "non-deterministic-finite-automata/run"))
    transitions = {("0", "a"): {"1", "2"}, ("1", "b"): {"3"}}
    assert automaton["accepts"]("ab", transitions, {"3"})
    assert not automaton["accepts"]("a", transitions, {"3"})
    assert automaton["accepts"]("", transitions, {"0"})
    for number in (1, 3):
        folder = FORMAL / "non-deterministic-finite-automata"
        rules, accepting = automaton["parse_automaton"](
            folder / f"automaton.{number}.txt"
        )
        actual = [
            "yes" if automaton["accepts"](line, rules, accepting) else "no"
            for line in (folder / f"in.{number}.txt").read_text().splitlines()
        ]
        assert actual == (folder / f"out.{number}.txt").read_text().splitlines()
    parser = subprocess.run(
        ["ruby", str(FORMAL / "recursive-grammar-parser/run")],
        input="0\n1+0+1\n10\n1+\n",
        capture_output=True,
        text=True,
        check=True,
    )
    assert parser.stdout.splitlines() == ["yes", "yes", "no", "no"], parser
    for directory in ["car-brands-regex", "palindromes-regex", "web-addresses-regex"]:
        folder = FORMAL / directory
        result = subprocess.run(
            ["bash", str(folder / "run")],
            input=(folder / "in.1.txt").read_text(),
            capture_output=True,
            text=True,
        )
        assert result.returncode in {0, 1}, result.stderr
        assert result.stdout.strip() == (folder / "out.1.txt").read_text().strip(), (
            directory,
            result.stdout,
        )
    subprocess.run(["ruby", str(ROOT / "tests/check_atm.rb")], check=True)
    print("Semester 5 checks passed")


if __name__ == "__main__":
    main()
