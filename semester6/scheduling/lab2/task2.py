def flatten_dependencies(groups):
    return [item for sublist in groups for item in sublist]


def find_available_task(order_dict, completed, n):
    selected = -1
    blocked = flatten_dependencies(list(order_dict.values()))

    for i in range(1, n + 1):
        if not (i in blocked) and not (i in completed):
            selected = i
            break

    return selected


def solver(n, m):
    time_dict = {}
    order_dict = {}
    total_time = 0

    for i in range(1, n + 1):
        time = int(input())
        time_dict[i] = time

    for i in range(m):
        predecessor, successor = list(map(int, input().split()))

        if not (predecessor in order_dict):
            order_dict[predecessor] = [successor]
        else:
            order_dict[predecessor].append(successor)

    completed = []

    while len(completed) != n:
        task = find_available_task(order_dict, completed, n)
        if task == -1:
            raise ValueError("Task dependencies contain a cycle")
        completed.append(task)

        total_time += time_dict[task]

        if task in order_dict:
            del order_dict[task]
        print(task)

    print(total_time)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    solver(n, m)
