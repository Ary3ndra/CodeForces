from math import sqrt
k = abs(input())
n = int((-1 + sqrt(1 + 8 * k + 0.9)) / 2)
if n * (n + 1) / 2 !=  k:
    n += 1
s = n * (n + 1) / 2
while (s - k) % 2 != 0:
    n += 1
    s += n
print n
