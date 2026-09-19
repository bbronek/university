import heapq


def minimum_penalty(machine_count, jobs):
    if machine_count <= 0 or any(
        weight < 0 or deadline < 0 for weight, deadline in jobs
    ):
        raise ValueError("Invalid machine count, weight, or deadline")
    selected = []
    for weight, deadline in sorted(jobs, key=lambda job: job[1]):
        heapq.heappush(selected, weight)
        if len(selected) > machine_count * deadline:
            heapq.heappop(selected)
    return sum(weight for weight, _ in jobs) - sum(selected)


if __name__ == "__main__":
    machines, count = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for _ in range(count)]
    print(minimum_penalty(machines, jobs))
