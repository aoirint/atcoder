import math
A, B = list(map(int, input().split(' ')))
a = 0.08
b = 0.10

x_min = math.floor(A / a)
x_max = math.ceil((A+1) / a)
y_min = math.floor(B / b)
y_max = math.ceil((B+1) / b)

X = set(range(x_min, x_max))
Y = set(range(y_min, y_max))

r = X & Y
R = min(r) if len(r) > 0 else -1
if len(r) == 1 and R == 0:
  R = -1

print(R)
# WA
