def spt_scheduling(m, n, processing_times):
    sorted_jobs = sorted(range(n), key=lambda x: processing_times[x])
    machine_loads = [0] * m
    job_completion_times = [0] * n

    for job in sorted_jobs:
        machine_idx = machine_loads.index(min(machine_loads))
        machine_loads[machine_idx] += processing_times[job]
        job_completion_times[job] = machine_loads[machine_idx]

    return sum(job_completion_times)


m, n = list(map(int, input().split()))
processing_times = []

for i in range(n):
    processing_times.append(int(input()))

total_completion_time = spt_scheduling(m, n, processing_times)

print(total_completion_time)
