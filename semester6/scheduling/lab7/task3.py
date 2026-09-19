def optimal_on_time_tasks(tasks):
    if any(
        duration <= 0 or weight < 0 or deadline < 0
        for duration, weight, deadline in tasks
    ):
        raise ValueError(
            "Expected positive durations and nonnegative weights and deadlines"
        )
    if not tasks:
        return 0, []
    ordered = sorted(enumerate(tasks, 1), key=lambda item: item[1][2])
    capacity = min(max(task[2] for task in tasks), sum(task[0] for task in tasks))
    best = [[0] * (capacity + 1) for _ in range(len(tasks) + 1)]
    take = [[False] * (capacity + 1) for _ in range(len(tasks) + 1)]
    for row, (_, (duration, weight, deadline)) in enumerate(ordered, 1):
        for available in range(capacity + 1):
            best[row][available] = best[row - 1][available]
            previous = min(available, deadline) - duration
            if (
                previous >= 0
                and best[row - 1][previous] + weight > best[row][available]
            ):
                best[row][available] = best[row - 1][previous] + weight
                take[row][available] = True
    selected = []
    available = capacity
    for row in range(len(tasks), 0, -1):
        if take[row][available]:
            index, (duration, _, deadline) = ordered[row - 1]
            selected.append(index)
            available = min(available, deadline) - duration
    return best[-1][-1], sorted(selected)


if __name__ == "__main__":
    count = int(input())
    tasks = [tuple(map(int, input().split())) for _ in range(count)]
    points, selected = optimal_on_time_tasks(tasks)
    print(points)
    for index in selected:
        print(index)
