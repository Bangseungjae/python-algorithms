i, j = input().split()
i = int(i)
j = int(j)

numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)
str_list = []
for i in range(j):
    s, e = map(int, input().split())
    str_list.append('{}\n'.format(prefix_sum[e] - prefix_sum[s - 1]))

print(''.join(str_list))