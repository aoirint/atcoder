N, M = list(map(int, input().split(' ')))
r = [ None for i in range(N) ]

illegal = False
for i in range(M):
  s, c = list(map(int, input().split(' ')))
  if r[s-1] is not None and r[s-1] != c:
    illegal = True
    break
  r[s-1] = c

v = -1
if not illegal:
  for i in range(N):
    if r[i] is None:
      if i == 0 and N != 1:
        r[i] = 1
      else:
        r[i] = 0
  v = sum(r[i] * 10**(N-1-i) for i in range(N))
  if v < 10**(N-1) and not (N == 1 and v == 0):
    v = -1

print(v)
