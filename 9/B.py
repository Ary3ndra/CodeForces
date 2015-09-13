from math import sqrt
n, vb, vs = map(int, raw_input().split())
stops = map(int, raw_input().split())
xu, yu = map(int, raw_input().split())
mini, mint = 0, 0
for i in range(n):
    t = float(stops[i]) / vb + sqrt((xu - stops[i]) ** 2 + yu ** 2) / vs
    if i == 1 or t < mint + 1e-5:
        mini, mint = i, t
print mini + 1
