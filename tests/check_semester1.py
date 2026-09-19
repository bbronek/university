from pathlib import Path
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SEMESTER = ROOT / "semester1"


def main():
    linked = runpy.run_path(
        str(SEMESTER / "algorithms-and-data-structures/python/linked_list.py")
    )["LinkedList"]()
    linked.insert_end(1)
    linked.insert_end(2)
    linked.insert_start(0)
    assert linked.remove(1)
    assert not linked.remove(7)
    assert linked.size() == 2
    assert linked.head.next_node.data == 2
    assert linked.remove(0) and linked.remove(2)
    assert linked.size() == 0 and linked.head is None

    tree_class = runpy.run_path(
        str(SEMESTER / "algorithms-and-data-structures/python/bst.py")
    )["BST"]
    for values in ([2], [2, 1], [2, 3], [2, 1, 3]):
        tree = tree_class()
        for value in values:
            tree.insert(value)
        tree.remove(2)
        remaining = [value for value in values if value != 2]
        assert tree.get_min() == (min(remaining) if remaining else None)
        assert tree.get_max() == (max(remaining) if remaining else None)

    multiply = runpy.run_path(
        str(SEMESTER / "programming-foundations/lab12/matrix_multiplication.py")
    )["multiply"]
    assert multiply([[1, 2], [3, 4]], [[5], [6]]) == [[17], [39]]

    scripts = [
        (
            "lab11/string_collection.py",
            "hello\nEND COLLECTION\nhello\nworld\n",
            "YES\nNO",
        ),
        ("lab11/longest_unique_string.py", "a\na\n", ""),
        ("lab12/hamming.py", "cat\n3\ncatastrophe\nbat\ncat\n", "cat"),
        ("lab13/traveling_salesperson.py", "0 0\n3 0\n3 4\n", "12.0"),
        ("lab13/pearson_correlation.py", "3\n1 2\n2 4\n3 6\n", "1.00"),
        ("lab10/number_sequences.py", "-3 4\ne\n", "-2 0 2 4"),
    ]
    for path, input_text, expected in scripts:
        result = subprocess.run(
            [sys.executable, str(SEMESTER / "programming-foundations" / path)],
            input=input_text,
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        assert result.stdout.strip() == expected, (path, result.stdout)

    with tempfile.TemporaryDirectory() as temporary:
        checks = [
            ("programming-foundations/lab9/two_largest.c", "3\n9 2 3\n", "9 3"),
            (
                "programming-foundations/lab9/two_largest_variant.c",
                "3\n-1 -1 -2\n",
                "-1 -1",
            ),
            (
                "algorithms-and-data-structures/c/lab4/merge_sort.c",
                "6\n2147483647 -1 0 5 5 -9\n",
                "-9 -1 0 5 5 2147483647",
            ),
            (
                "algorithms-and-data-structures/c/lab1/max_number_with_index.c",
                "3\n-9 -3 -8\n",
                "-3 2",
            ),
            ("algorithms-and-data-structures/c/lab1/perfect_number.c", "1\n", "no"),
            (
                "algorithms-and-data-structures/c/lab6/queue_linkedlist.c",
                "1\n6\n9 2 0 0 0 5\n",
                "9\n2\nempty",
            ),
            ("programming-foundations/lab5/count_maximum.c", "5\n2 1 3 3 3\n", "3"),
            (
                "algorithms-and-data-structures/c/lab5/queue.cpp",
                "ENQUEUE 1\nDEQUEUE\n" * 150 + "ENQUEUE 9\nEND\n",
                "9",
            ),
        ]
        for index, (path, input_text, expected) in enumerate(checks):
            binary = str(Path(temporary) / str(index))
            compiler = "g++" if path.endswith(".cpp") else "gcc"
            subprocess.run(
                [compiler, "-fsanitize=undefined", str(SEMESTER / path), "-o", binary],
                check=True,
            )
            result = subprocess.run(
                [binary],
                input=input_text,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
            assert not result.stderr, result.stderr
            assert result.stdout.strip() == expected, (path, result.stdout)
        shell = str(Path(temporary) / "microshell")
        subprocess.run(
            [
                "gcc",
                "-Wall",
                "-Wextra",
                "-Werror",
                str(SEMESTER / "operating-systems/microshell/microshell.c"),
                "-o",
                shell,
            ],
            check=True,
        )
        result = subprocess.run(
            [shell],
            input='printf "%s" "hello world"\n\nexit\n',
            text=True,
            capture_output=True,
            check=True,
            timeout=5,
        )
        assert result.stdout == "hello world", result
    print("Semester 1 checks passed")


if __name__ == "__main__":
    main()
