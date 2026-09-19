from itertools import combinations, permutations
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
SEMESTER = ROOT / "semester6"


def main():
    load = lambda path: runpy.run_path(str(SEMESTER / path))
    rsa = load("elements-of-cryptanalysis/week-5/rsa_chinese_remainder.py")
    public, private = rsa["generate_keypair"](61, 53)
    for message in (0, 1, 53, 61, 123, 3232):
        encrypted = pow(message, *public)
        assert rsa["decrypt_crt"](encrypted, 61, 53, private[0]) == message
    elgamal = load("elements-of-cryptanalysis/week-6/elgamal.py")
    generator, public_key, private_key = elgamal["generate_keys"](467)
    for message in (0, 1, 123, 466):
        first, second = elgamal["encrypt"](generator, public_key, 467, message)
        assert elgamal["decrypt"](first, second, 467, private_key) == message
    assert not elgamal["is_prime"](561)
    weighted = load("scheduling/lab1/task2.py")["weighted_completion_cost"]
    jobs = [(3, 2), (1, 4), (0, 3)]

    def cost(order):
        elapsed = total = 0
        for duration, weight in order:
            elapsed += duration
            total += elapsed * weight
        return total

    assert weighted(jobs) == min(map(cost, permutations(jobs)))
    assert load("scheduling/lab7/task1.py")["partition_work"]([2, 3, 7]) == (5, 7)
    assert (
        load("scheduling/lab6/task3.py")["minimum_penalty"](
            1, [(10, 1), (5, 1), (9, 2)]
        )
        == 5
    )
    optimal = load("scheduling/lab7/task3.py")["optimal_on_time_tasks"]
    tasks = [(3, 7, 5), (2, 9, 2), (1, 2, 1), (1, 5, 6)]
    expected = 0
    for length in range(len(tasks) + 1):
        for subset in combinations(tasks, length):
            elapsed = 0
            for duration, _, deadline in sorted(subset, key=lambda task: task[2]):
                elapsed += duration
                if elapsed > deadline:
                    break
            else:
                expected = max(expected, sum(task[1] for task in subset))
    score, selected = optimal(tasks)
    assert score == expected == sum(tasks[index - 1][1] for index in selected)
    assert optimal([]) == (0, [])
    neh = load("scheduling/lab10/task2.py")["neh_algorithm"]
    assert neh(2, 0, []) == (0, [])
    assert neh(2, 1, [[3, 5]]) == (8, [1])
    assert load("scheduling/lab10/task1.py")["three_machine_schedule"]([(2, 3, 4)]) == 9
    print("Semester 6 checks passed")


if __name__ == "__main__":
    main()
