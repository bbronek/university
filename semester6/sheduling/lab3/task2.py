def calculate_cost(time_dict, time, task):
    return time_dict[task][1]*time*time+time_dict[task][2]*time+time_dict[task][3]

def solver():
    n = int(input())
    times = 0
    time_dict = {}
    order_dict = {}
    succ_number = {}
    available_tasks = []
    maksymilian = 0

    for i in range(1, n+1):
        p, a, b, c = list(map(int, input().split()))
        time_dict[i] = [p, a, b, c]
        times += p
        succ_number[i] = 0
        order_dict[i] = []

    e = int(input())

    for i in range(1, e+1):
        k, l = list(map(int, input().split()))
        order_dict[l].append(k)

        succ_number[k] += 1

    for i in range(1, n+1):
        for i in range(1, n+1):
            if succ_number[i] == 0:
                available_tasks.append(i)
                succ_number[i] = -1

        min = calculate_cost(time_dict, times, available_tasks[0])
        mini = 0

        for i in range(1, len(available_tasks)):
            cost = calculate_cost(time_dict, times, available_tasks[i])

            if cost <= min:
                min = cost
                mini = i

        if min >= maksymilian:
            maksymilian = min

        for x in order_dict[available_tasks[mini]]:
            succ_number[x] -= 1

        times -= time_dict[available_tasks[mini]][0]
        del available_tasks[mini]

    print(maksymilian)

if __name__ == '__main__':
    solver()