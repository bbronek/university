def flatten(l):
    return [item for sublist in l for item in sublist]

def sort_dict(d):
    sorted_by_priority = sorted(d.items(), key=lambda x:x[1][0])
    converted_dict = dict(sorted_by_priority)

    return converted_dict

def find_available_task(time_dict, order_dict, done_tasks, n):
    chosen_one = -1
    blocked = flatten(list(order_dict.values()))

    for t in time_dict:
        if not (t in blocked) and not (t in done_tasks):
            chosen_one = t
            break
    return chosen_one

def solver():
    time_dict = {}
    order_dict = {}
    total_time = 0

    n = int(input())

    for i in range(1, n + 1):
        r, p = list(map(int, input().split()))
        time_dict[i] = [r, p]

    e = int(input())

    for i in range(1, e + 1):
        k, l = list(map(int, input().split()))
        if not (k in order_dict):
            order_dict[k] = [l]
        else:
            order_dict[k].append(l)

    time_dict = sort_dict(time_dict)

    done_tasks = []

    while len(done_tasks) != n:
        t = find_available_task(time_dict, order_dict, done_tasks, n)
        done_tasks.append(t)

        if total_time < time_dict[t][0]:
            total_time = time_dict[t][0]

        total_time += time_dict[t][1]

        if t in order_dict:
            del order_dict[t]

    print(total_time)


if __name__ == '__main__':
    solver()
