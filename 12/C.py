n, m = map(int, raw_input().split())
price = map(int, raw_input().split())
price.sort()
d = {}
for i in range(m):
    s = raw_input()
    d[s] = d.get(s, 0) + 1
fruits = sorted(d, key = lambda x: d[x], reverse = True)
m, M = 0, 0
for i, f in enumerate(fruits):
    m += price[i] * d[f]
    M += price[-i - 1] * d[f]

print m, M
