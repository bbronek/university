def makespan(sequence, orders, machine_count):
    completion = [0] * machine_count
    for job in sequence:
        for machine in range(machine_count):
            previous = completion[machine - 1] if machine else 0
            completion[machine] = (
                max(completion[machine], previous) + orders[job - 1][machine]
            )
    return completion[-1] if completion else 0


def neh_algorithm(machine_count, job_count, orders):
    if machine_count <= 0 or job_count != len(orders):
        raise ValueError("Invalid machine or job count")
    if any(
        len(order) != machine_count or any(time < 0 for time in order)
        for order in orders
    ):
        raise ValueError("Invalid processing times")
    ranked = sorted(
        range(1, job_count + 1), key=lambda job: sum(orders[job - 1]), reverse=True
    )
    sequence = []
    for job in ranked:
        candidates = [
            sequence[:position] + [job] + sequence[position:]
            for position in range(len(sequence) + 1)
        ]
        sequence = min(
            candidates, key=lambda candidate: makespan(candidate, orders, machine_count)
        )
    return makespan(sequence, orders, machine_count), sequence


if __name__ == "__main__":
    machines, count = map(int, input().split())
    orders = [list(map(int, input().split())) for _ in range(count)]
    total, sequence = neh_algorithm(machines, count, orders)
    print(total)
    print(*sequence)
