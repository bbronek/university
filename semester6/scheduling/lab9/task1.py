def main():
    n_tasks = int(input())
    longest_job = 0
    sum_p1 = 0
    sum_p2 = 0
    for i in range(n_tasks):
        p1, p2 = map(int, input().split())
        longest_job = max(longest_job, p1 + p2)
        sum_p1 += p1
        sum_p2 += p2
    p = max(sum_p1, sum_p2)
    makespan = max(longest_job, p)
    print(makespan)


if __name__ == "__main__":
    main()
