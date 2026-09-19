def flatten_dependencies(groups):
    return [item for group in groups for item in group]


def sort_dict(mapping):
    sorted_by_priority = sorted(mapping.items(), key=lambda x: x[1][0])
    converted_dict = dict(sorted_by_priority)

    return converted_dict


def find_available_task(time_dict, order_dict, completed, n):
    selected = -1
    blocked = flatten_dependencies(list(order_dict.values()))

    for task in time_dict:
        if not (task in blocked) and not (task in completed):
            selected = task
            break
    return selected


def solver():
    time_dict = {}
    order_dict = {}
    total_time = 0

    n = int(input())

    for i in range(1, n + 1):
        release_time, processing_time = list(map(int, input().split()))
        time_dict[i] = [release_time, processing_time]

    e = int(input())

    for i in range(1, e + 1):
        predecessor, successor = list(map(int, input().split()))
        if not (predecessor in order_dict):
            order_dict[predecessor] = [successor]
        else:
            order_dict[predecessor].append(successor)

    time_dict = sort_dict(time_dict)

    completed = []

    while len(completed) != n:
        task = find_available_task(time_dict, order_dict, completed, n)
        if task == -1:
            raise ValueError("Task dependencies contain a cycle")
        completed.append(task)

        if total_time < time_dict[task][0]:
            total_time = time_dict[task][0]

        total_time += time_dict[task][1]

        if task in order_dict:
            del order_dict[task]

    print(total_time)


if __name__ == "__main__":
    solver()
