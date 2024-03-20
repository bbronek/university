def min_delayed_weight(n, tasks):
    tasks = sorted(tasks, key=lambda x: x[2])
    deadlines = [task[2] for task in tasks]

    F = [[0] * (deadlines[-1] + 1) for _ in range(n + 1)]
    path = [[None] * (deadlines[-1] + 1) for _ in range(n + 1)]

    for j in range(n + 1):
        for t in range(deadlines[-1] + 1):
            if j == 0:
                F[j][t] = 0
            elif t == 0:
                F[j][t] = sum(task[1] for task in tasks[:j])
            elif t <= deadlines[j - 1]:
                if t >= tasks[j - 1][0]:
                    F[j][t] = min(F[j - 1][t - tasks[j - 1][0]], F[j - 1][t] + tasks[j - 1][1])
                    if F[j - 1][t - tasks[j - 1][0]] <= F[j - 1][t] + tasks[j - 1][1]:
                        path[j][t] = (j - 1, t - tasks[j - 1][0], True)
                    else:
                        path[j][t] = (j - 1, t, False)
                else:
                    F[j][t] = F[j - 1][t] + tasks[j - 1][1]
                    path[j][t] = (j - 1, t, False)
            else:
                F[j][t] = F[j][deadlines[j - 1]]
                path[j][t] = (j, deadlines[j - 1], False)

    return F[n][deadlines[-1]], path


def extract_selected_tasks(tasks, path):
    selected_tasks = []
    j, t = len(tasks), tasks[-1][2]

    while j > 0:
        prev_j, prev_t, selected = path[j][t]
        if selected:
            selected_tasks.append(j)
        j, t = prev_j, prev_t

    return sorted(selected_tasks)


def main():
    n = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(n)]

    min_weight, path = min_delayed_weight(n, tasks)
    max_points = sum(task[1] for task in tasks) - min_weight

    print(max_points)

    selected_tasks = extract_selected_tasks(tasks, path)
    for task_idx in selected_tasks:
        print(task_idx)


if __name__ == '__main__':
    main()