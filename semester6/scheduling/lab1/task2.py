from fractions import Fraction


def weighted_completion_cost(jobs):
    if any(duration < 0 or weight < 0 for duration, weight in jobs):
        raise ValueError("Durations and weights must be nonnegative")
    ordered = sorted(
        jobs, key=lambda job: Fraction(job[0], job[1]) if job[1] else float("inf")
    )
    elapsed = total = 0
    for duration, weight in ordered:
        elapsed += duration
        total += elapsed * weight
    return total


if __name__ == "__main__":
    count = int(input())
    print(
        weighted_completion_cost(
            [tuple(map(int, input().split())) for _ in range(count)]
        )
    )
