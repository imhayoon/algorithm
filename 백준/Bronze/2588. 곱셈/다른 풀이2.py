
N = int(input())
m = int(input())
M = list(map(int, str(m)))

o = [-1, -2, 0]

for i in o:
    print(i, N * M[i])
    
print(N*m)
