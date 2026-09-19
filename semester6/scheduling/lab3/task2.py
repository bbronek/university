def calculate_cost(jobs, time, task):
    return jobs[task][1] * time * time + jobs[task][2] * time + jobs[task][3]


def solver():
    n = int(input())
    remaining_time = 0
    jobs = {}
    predecessors = {}
    successor_count = {}
    available_tasks = []
    maximum_cost = 0

    for i in range(1, n + 1):
        p, a, b, c = list(map(int, input().split()))
        jobs[i] = [p, a, b, c]
        remaining_time += p
        successor_count[i] = 0
        predecessors[i] = []

    e = int(input())

    for i in range(1, e + 1):
        k, l = list(map(int, input().split()))
        predecessors[l].append(k)

        successor_count[k] += 1

    for i in range(1, n + 1):
        for i in range(1, n + 1):
            if successor_count[i] == 0:
                available_tasks.append(i)
                successor_count[i] = -1

        if not available_tasks:
            raise ValueError("Task dependencies contain a cycle")
        minimum_cost = calculate_cost(jobs, remaining_time, available_tasks[0])
        selected_index = 0

        for i in range(1, len(available_tasks)):
            cost = calculate_cost(jobs, remaining_time, available_tasks[i])

            if cost <= minimum_cost:
                minimum_cost = cost
                selected_index = i

        if minimum_cost >= maximum_cost:
            maximum_cost = minimum_cost

        for x in predecessors[available_tasks[selected_index]]:
            successor_count[x] -= 1

        remaining_time -= jobs[available_tasks[selected_index]][0]
        del available_tasks[selected_index]

    print(maximum_cost)


if __name__ == "__main__":
    solver()
