def partition_work(processing_times):
    if any(duration < 0 for duration in processing_times):
        raise ValueError("Processing times must be nonnegative")
    total = sum(processing_times)
    capacity = total // 2
    best = [0] * (capacity + 1)
    for duration in processing_times:
        for available in range(capacity, duration - 1, -1):
            best[available] = max(
                best[available], best[available - duration] + duration
            )
    return best[capacity], total - best[capacity]


if __name__ == "__main__":
    count = int(input())
    print(*partition_work([int(input()) for _ in range(count)]))
