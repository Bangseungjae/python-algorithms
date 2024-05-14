n = input()
A = []

for i in range(int(n)):
    A.append(int(input()))

A.sort()
print('\n'.join(map(str, A)))
