def three_machine_schedule(jobs):
    if any(len(job) != 3 or any(time < 0 for time in job) for job in jobs):
        raise ValueError("Expected three nonnegative processing times per job")
    early = sorted(
        (job for job in jobs if job[0] <= job[2]), key=lambda job: job[0] + job[1]
    )
    late = sorted(
        (job for job in jobs if job[0] > job[2]),
        key=lambda job: job[1] + job[2],
        reverse=True,
    )
    completion = [0, 0, 0]
    for job in early + late:
        for machine, duration in enumerate(job):
            previous = completion[machine - 1] if machine else 0
            completion[machine] = max(completion[machine], previous) + duration
    return completion[-1]


if __name__ == "__main__":
    count = int(input())
    print(
        three_machine_schedule([tuple(map(int, input().split())) for _ in range(count)])
    )
