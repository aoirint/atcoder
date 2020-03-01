N, M, K = list(map(int, input().split(' ')))
AB = []
for i in range(M):
  ab = set(map(int, input().split(' ')))
  AB.append(ab)

CD = []
for i in range(K):
  cd = set(map(int, input().split(' ')))
  CD.append(cd)

def friends(i):
  ret = []
  for a, b in AB:
    if a == i:
      ret.append(b)
    elif b == i:
      ret.append(a)
  return list(set(ret))

def tree(i, x):
  i_friends = friends(i)
  x.extend(i_friends)
  for # TIMEUP:


for i in range(N):
  result = [ 1 for _ in range(N) ]
  for j in range(N):
    if i == j:
      result[j] = 0
      continue
    if set([i, j]) in AB:
      result[j] = 0
      continue
    if set([i, j]) in CD:
      result[j] = 0
      continue

    result = sum(result)
  print(result)
