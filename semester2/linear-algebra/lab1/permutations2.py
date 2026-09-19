from math import lcm


def cycles(permutation):
    if sorted(permutation) != list(range(1, len(permutation) + 1)):
        raise ValueError("Expected a permutation of 1 through n")
    visited = set()
    result = []
    for start in range(1, len(permutation) + 1):
        if start in visited:
            continue
        cycle = []
        current = start
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = permutation[current - 1]
        if len(cycle) > 1:
            result.append(cycle)
    return result


def main():
    count = int(input())
    permutation = list(map(int, input().split()))
    if len(permutation) != count:
        raise ValueError("Unexpected permutation length")
    result = cycles(permutation)
    print("".join("(" + ",".join(map(str, cycle)) + ")" for cycle in result) or "()")
    print(lcm(*(len(cycle) for cycle in result)))
    print(
        "".join(
            f"({cycle[0]},{value})" for cycle in result for value in reversed(cycle[1:])
        )
    )
    print("odd" if sum(len(cycle) - 1 for cycle in result) % 2 else "even")


if __name__ == "__main__":
    main()
