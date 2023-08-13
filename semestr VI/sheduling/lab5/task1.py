def choose_available_official(oficials_times):
    return oficials_times.index(min(oficials_times))


m, n = map(int, input().split())

officials_times = [0 for i in range(m)]
tasks = []

for i in range(n):
    tasks.append(int(input()))

available_official = 0

tasks.sort(reverse=True)

for task in tasks:
    officials_times[available_official] += task
    available_official = choose_available_official(officials_times)

print(max(officials_times))