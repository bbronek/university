def neh_algorithm(M, N, orders):
    order_times = list(zip(range(1, N + 1), [sum(order) for order in orders]))
    order_times.sort(key=lambda x: x[1], reverse=True)

    sequence = [order_times[0][0]]
    del order_times[0]

    def calculate_total_time(sequence):
        time_table = [[0 for _ in range(M)] for _ in range(len(sequence))]

        for i in range(len(sequence)):
            for j in range(M):
                if i == 0 and j == 0:
                    time_table[i][j] = orders[sequence[i] - 1][j]
                elif i == 0:
                    time_table[i][j] = time_table[i][j - 1] + orders[sequence[i] - 1][j]
                elif j == 0:
                    time_table[i][j] = time_table[i - 1][j] + orders[sequence[i] - 1][j]
                else:
                    time_table[i][j] = max(time_table[i - 1][j], time_table[i][j - 1]) + orders[sequence[i] - 1][j]

        return time_table[-1][-1]

    while order_times:
        best_sequence = sequence.copy()
        best_time = float("inf")

        for i in range(len(sequence) + 1):
            temp_sequence = sequence.copy()
            temp_sequence.insert(i, order_times[0][0])

            temp_time = calculate_total_time(temp_sequence)
            if temp_time < best_time:
                best_time = temp_time
                best_sequence = temp_sequence

        sequence = best_sequence
        del order_times[0]

    return best_time, sequence


M, N = map(int, input().strip().split())
orders = []
for _ in range(N):
    order = list(map(int, input().strip().split()))
    orders.append(order)

total_time, sequence = neh_algorithm(M, N, orders)

print(total_time)
print(' '.join(map(str, sequence)))
