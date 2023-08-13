def calculate_cij(task, employee, toy):
    c = [[0 for _ in range(employee+1)] for _ in range(toy+1)]
    for i in range(1, toy+1):
        for j in range(1, employee+1):
            if j == 1:
                c[i][j] = c[i-1][j] + task[i-1][j-1]
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1]) + task[i-1][j-1]
    return c

def main():
    employee, toy = map(int, input().split())
    task = []
    for _ in range(toy):
        task.append([int(x) for x in input().split()])
    c = calculate_cij(task, employee, toy)
    for i in range(1, toy+1):
        print(c[i][employee])

if __name__ == "__main__":
    main()