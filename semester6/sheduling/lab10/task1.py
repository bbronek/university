item_count = int(input())

param_dict = dict()
group_lesser = dict()
group_greater = dict()

sum_p2 = 0

for idx in range(item_count):
    param1, param2, param3 = map(int, input().split())
    param_dict[idx] = [param1 + param2, param2 + param3]
    sum_p2 += param2

for index, [sum1, sum2] in param_dict.items():
    if sum1 <= sum2:
        group_lesser[index] = [sum1, sum2]
    else:
        group_greater[index] = [sum1, sum2]

group_lesser = sorted(group_lesser.items(), key=lambda x: x[1][0])
group_greater = sorted(group_greater.items(), key=lambda x: x[1][1], reverse=True)

queue = group_lesser + group_greater

timing = [0, queue[0][1][0]]

for index, (time1, time2) in queue:
    timing[0] += time1
    if timing[1] < timing[0]:
        timing[1] = timing[0]
    timing[1] += time2

print(timing[1] - sum_p2)
