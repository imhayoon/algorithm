N = int(input())
M = list(map(int, input()))


print(N * M[-1])
print(N * M[-2])
print(N * M[0])
print((N*M[-1]) + (N * M[-2] * 10) + (N * M[0] * 100))