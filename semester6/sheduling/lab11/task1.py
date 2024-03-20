import random


def calculate_total_time(order, times):
    m = len(times[0])
    n = len(order)
    total_time = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                total_time[i][j] = times[order[i]][j]
            elif i == 0:
                total_time[i][j] = total_time[i][j - 1] + times[order[i]][j]
            elif j == 0:
                total_time[i][j] = total_time[i - 1][j] + times[order[i]][j]
            else:
                total_time[i][j] = max(total_time[i - 1][j], total_time[i][j - 1]) + times[order[i]][j]

    return total_time[-1][-1]


def generate_neighborhood(order):
    neighborhood = []

    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            neighbor = order[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighborhood.append(neighbor)

    return neighborhood


def local_search(toy_times):
    order = list(range(len(toy_times)))
    random.shuffle(order)
    current_time = calculate_total_time(order, toy_times)

    while True:
        neighborhood = generate_neighborhood(order)
        best_time = current_time
        best_order = None
        for neighbor in neighborhood:
            neighbor_time = calculate_total_time(neighbor, toy_times)
            if neighbor_time < best_time:
                best_time = neighbor_time
                best_order = neighbor
        if best_order is not None:
            order = best_order
            current_time = best_time
        else:
            break

    return current_time, [i + 1 for i in order]


def main():
    m, n = map(int, input().split())
    toy_times = [list(map(int, input().split())) for _ in range(n)]
    total_time, order = local_search(toy_times)

    print(total_time)
    print(' '.join(map(str, order)))


if __name__ == "__main__":
    main()
