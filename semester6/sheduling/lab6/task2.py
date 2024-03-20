num_workers, num_jobs = map(int, input().split())
worker_speeds = list(map(int, input().split()))
job_durations = []
for i in range(num_jobs):
    job_durations.append(int(input()))
job_durations = sorted(job_durations, reverse=True)

assigned_jobs = [[] for _ in range(num_workers)]
worker_times = []
for speed in worker_speeds:
    worker_times.append(speed)
    assigned_jobs.append([])

job_index = 0
for job_duration in job_durations:
    job_index += 1
    min_worker_time = min(worker_times)
    min_worker_index = worker_times.index(min_worker_time)

    for i in range(len(assigned_jobs[min_worker_index])):
        assigned_jobs[min_worker_index][i] += (job_duration * worker_speeds[min_worker_index])

    assigned_jobs[min_worker_index].insert(0, (job_duration * worker_speeds[min_worker_index]))
    worker_times[min_worker_index] = min_worker_time + worker_speeds[min_worker_index]

total_time = 0
for i in range(num_workers):
    total_time += sum(assigned_jobs[i])
print(total_time)
