def optimal_tasks(n, D, tasks):
    A = [[0] * (D + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, D + 1):
            time, points = tasks[i - 1]
            if time <= j:
                A[i][j] = max(A[i - 1][j], A[i - 1][j - time] + points)
            else:
                A[i][j] = A[i - 1][j]

    max_points = A[n][D]

    selected_tasks = []
    j = D
    for i in range(n, 0, -1):
        if A[i][j] != A[i - 1][j]:
            selected_tasks.append(i)
            j -= tasks[i - 1][0]

    return max_points, sorted(selected_tasks)


def main():
    n, D = map(int, input().split())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]

    max_points, selected_tasks = optimal_tasks(n, D, tasks)

    print(max_points)
    for task in selected_tasks:
        print(task)

if __name__ == '__main__':
    main()