def flatten(l):
    return [item for sublist in l for item in sublist]


def find_available_task(order_dict, done_tasks, n):
    chosen_one = -1
    blockers = flatten(list(order_dict.values()))

    for i in range(1, n + 1):
        if not (i in blockers) and not (i in done_tasks):
            chosen_one = i
            break

    return chosen_one


def solver(n, m):
    time_dict = {}
    order_dict = {}
    total_time = 0

    for i in range(1, n + 1):
        time = int(input())
        time_dict[i] = time

    for i in range(m):
        succ, pre = list(map(int, input().split()))

        if not (succ in order_dict):
            order_dict[succ] = [pre]
        else:
            order_dict[succ].append(pre)

    done_tasks = []

    while len(done_tasks) != n:
        t = find_available_task(order_dict, done_tasks, n)
        done_tasks.append(t)

        total_time += time_dict[t]

        if t in order_dict:
            del order_dict[t]
        print(t)

    print(total_time)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    solver(n, m)