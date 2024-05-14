N = int(input())

M = str(input())
M = M.split(" ")
M = list(map(int, M))
rs = 0
max_score = max(M)
for i in range(N):
    M[i] = M[i] / max_score * 100
print(sum(M) / N)
