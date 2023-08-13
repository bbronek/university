def johnson_algorithm(tasks):
    tasks_A = sorted((p for p in tasks if p[1][0] <= p[1][1]), key=lambda x: x[1][0])
    tasks_B = sorted((p for p in tasks if p[1][0] > p[1][1]), key=lambda x: x[1][1], reverse=True)

    tasks_sorted = tasks_A + tasks_B
    time1, time2 = 0, 0
    schedule = []

    for idx, task in tasks_sorted:
        time1 += task[0]
        time2 = max(time2, time1) + task[1]
        schedule.append((idx + 1, time1, time2))

    return schedule


def main():
    n = int(input())
    tasks = [(i, list(map(int, input().split()))) for i in range(n)]
    schedule = johnson_algorithm(tasks)
    for s in schedule:
        print(*s)


if __name__ == "__main__":
    main()