R = 3
r = [ list(map(int, input().split(' '))) for i in range(R) ]

def check():
  for y in range(R):
    f = True
    for x in range(R):
      if r[y][x] != 0:
        f = False
        break
    if f:
      return True

  for x in range(R):
    f = True
    for y in range(R):
      if r[y][x] != 0:
        f = False
        break
    if f:
      return True

  f = True
  for p in range(R):
    if r[p][p] != 0:
      f = False
      break
  if f:
    return True

  f = True
  for p in range(R):
    if r[R-1-p][p] != 0:
      f = False
      break
  return f

N = int(input())
for i in range(N):
  v = int(input())

  for y in range(R):
    for x in range(R):
      if r[y][x] == v:
        r[y][x] = 0

print('Yes' if check() else 'No')
