n = int(input())
orders = []
for i in range(n):
    p, d = map(int, input().split())
    orders.append((p, d))

orders.sort(key=lambda x: x[1])
max_delay = -1000
current_time = 0

for p, d in orders:
    current_time += p
    delay = current_time - d

    if delay > max_delay:
        max_delay = delay

print(max_delay)