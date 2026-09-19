def multiply(first, second):
    if not first or not second or not second[0]:
        raise ValueError("Matrices must be nonempty")
    inner = len(second)
    columns = len(second[0])
    if any(len(row) != inner for row in first) or any(
        len(row) != columns for row in second
    ):
        raise ValueError("Incompatible matrix dimensions")
    return [
        [
            sum(left * right for left, right in zip(row, column))
            for column in zip(*second)
        ]
        for row in first
    ]


def read_matrix():
    rows, columns = map(int, input().split())
    if rows <= 0 or columns <= 0:
        raise ValueError("Matrix dimensions must be positive")
    matrix = [list(map(float, input().split())) for _ in range(rows)]
    if any(len(row) != columns for row in matrix):
        raise ValueError("Unexpected row length")
    return matrix


def main():
    try:
        first = read_matrix()
        second = read_matrix()
        result = multiply(first, second)
    except ValueError:
        print("ERROR")
        return
    for row in result:
        print(" ".join(f"{value:.1f}" for value in row))


if __name__ == "__main__":
    main()
