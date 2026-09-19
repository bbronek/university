def calculate_cij(processing_times, machine_count, job_count):
    completion_times = [
        [0 for _ in range(machine_count + 1)] for _ in range(job_count + 1)
    ]
    for i in range(1, job_count + 1):
        for j in range(1, machine_count + 1):
            if j == 1:
                completion_times[i][j] = (
                    completion_times[i - 1][j] + processing_times[i - 1][j - 1]
                )
            else:
                completion_times[i][j] = (
                    max(completion_times[i - 1][j], completion_times[i][j - 1])
                    + processing_times[i - 1][j - 1]
                )
    return completion_times


def main():
    machine_count, job_count = map(int, input().split())
    processing_times = []
    for _ in range(job_count):
        processing_times.append([int(x) for x in input().split()])
    completion_times = calculate_cij(processing_times, machine_count, job_count)
    for i in range(1, job_count + 1):
        print(completion_times[i][machine_count])


if __name__ == "__main__":
    main()
