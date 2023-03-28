N = int(input())
m = int(input())
M = list(map(int, str(m)))

for i in range(3):
    print(N * M[2-i])

print(N*m)
