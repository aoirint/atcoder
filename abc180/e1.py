import math
import numpy as np

def calc_cost(x, y):
    a, b, c = x
    p, q, r = y
    return abs(p - a) + abs(q - b) + max(0, r - c)

# Thanks: https://github.com/kanchi0914/TSP/blob/master/2-opt-algorithm.py
def nearest_n(data, datalen, root, ex_root):
    root.append(0)
    ex_root.remove(0)

    for i in range(datalen - 1):
        min_len = 0
        min_Num = 0
        for j in range(len(ex_root)):
            if j == 0 or min_len > calc_cost(data[root[i]], data[ex_root[j]]):
                min_len = calc_cost(data[root[i]], data[ex_root[j]])
                min_Num = ex_root[j]
        root.append(min_Num)
        ex_root.remove(min_Num)

    return root

def opt_2(data, datalen, root):
    total = 0
    while True:
        count = 0
        for i in range(datalen - 2):
            i1 = i + 1
            for j in range(i + 2, datalen):
                if j == datalen - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = calc_cost(data[root[i]], data[root[i1]])
                    l2 = calc_cost(data[root[j]], data[root[j1]])
                    l3 = calc_cost(data[root[i]], data[root[j]])
                    l4 = calc_cost(data[root[i1]], data[root[j1]])
                    if l1 + l2 > l3 + l4:
                        new_root = root[i1:j+1]
                        root[i1:j+1] = new_root[::-1]
                        count += 1
        total += count
        if count == 0: break

    return root

def cal_totalcost(data, root):
    totalcost = 0
    for i in range(len(root)):
        totalcost += calc_cost(data[root[i]], data[root[i-1]])
    return totalcost

root = []
ex_root = []

N = int(input())
lines = [ list(map(int, input().split(' '))) for i in range(N) ]
data = np.zeros((N, 3), dtype=np.int32)
for i in range(N):
    ex_root.append(i)
    sp = lines[i]
    data[i,0] = sp[0]
    data[i,1] = sp[1]
    data[i,2] = sp[2]

root = nearest_n(data, N, root, ex_root)
root = opt_2(data, N, root)
cost = cal_totalcost(data, root)
print(cost)
