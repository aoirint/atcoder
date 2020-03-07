import math
N, A, B = list(map(int, input().split(' ')))
S = A + B
count = N // S if S != 0 else 0
mod = min(N % S, A) if S != 0 else 0
print(A*count + mod)
