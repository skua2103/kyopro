N = int(input())

parts_info = [list(map(int, input().split())) for _ in range(N)]

happiness_difference = []
head_weight = 0
body_weight = 0
total_happiness = 0
for i in range(N):
    if parts_info[i][1] <= parts_info[i][2]:
        total_happiness += parts_info[i][2]
        body_weight += parts_info[i][0]
    else:
        total_happiness += parts_info[i][1]
        head_weight += parts_info[i][0]
        difference = parts_info[i][1] - parts_info[i][2]
        rate = difference / parts_info[i][0]
        happiness_difference.append([i, difference, rate])


j = 0
happiness_difference.sort(key=lambda x: x[2])
while head_weight > body_weight:
    head_weight -= parts_info[happiness_difference[j][0]][0]
    body_weight += parts_info[happiness_difference[j][0]][0]
    total_happiness -= happiness_difference[j][1]
    j += 1
if body_weight >= head_weight:
    print(total_happiness)
