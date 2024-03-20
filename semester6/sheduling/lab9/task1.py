n_tasks = int(input())
sum_tasks = 0
sum_p1 = 0
sum_p2 = 0
for i in range(n_tasks):
    p1, p2 = map(int, input().split())
    sum_tasks = max(sum_tasks,p1+p2)
    sum_p1 += p1
    sum_p2 += p2
p = max(sum_p1,sum_p2)
cMax = max(sum_tasks,p)
print(cMax)
