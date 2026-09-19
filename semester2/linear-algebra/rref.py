def rref(matrix, tolerance=1e-12):
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive")
    if not matrix:
        return []
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("Matrix rows must have equal lengths")
    result = [list(map(float, row)) for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = max(
            range(pivot_row, len(result)), key=lambda row: abs(result[row][column])
        )
        if abs(result[pivot][column]) <= tolerance:
            continue
        result[pivot_row], result[pivot] = result[pivot], result[pivot_row]
        divisor = result[pivot_row][column]
        result[pivot_row] = [value / divisor for value in result[pivot_row]]
        for row in range(len(result)):
            if row != pivot_row:
                factor = result[row][column]
                result[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(result[row], result[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(result):
            break
    return result


if __name__ == "__main__":
    rows, columns = map(int, input().split())
    matrix = [list(map(float, input().split())) for _ in range(rows)]
    if any(len(row) != columns for row in matrix):
        raise ValueError("Unexpected number of columns")
    print(rref(matrix))
