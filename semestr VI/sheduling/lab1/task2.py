def calculate_cost(n):
    v = []
    v_priority = []
    result = 0

    for i in range(n):
        x = input()
        v.append(list(map(int, x.split())))

    for i, x in enumerate(v):
        v_priority.append([x[1]/x[0], i])

    performance_order = sorted(v_priority, key=lambda x: x[0], reverse=True)

    for x in performance_order:
        index = x[1]
        days = v[index][0]

        result += count_delay_cost(v, days)
        v[index] = [0, 0]

    return result


def count_delay_cost(v, days):
    iteration_result = 0

    for i in range(len(v)):
        iteration_result += days * v[i][1]

    return iteration_result


if __name__ == '__main__':
    n = int(input())

    response = calculate_cost(n)

    print(response)
