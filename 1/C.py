from math import sqrt, acos, fmod, sin, pi
p = []
for i in range(3):
    p.append(map(float, raw_input().split()))

theta = []

def length(a):
    return sqrt(a[0] ** 2 + a[1] ** 2)

def inner_product(a, b):
    return a[0] * b[0] + a[1] * b[1]

for i in range(3):
    v = []
    for j in range(3):
        if j != i:
            v.append((p[j][0] - p[i][0], p[j][1] - p[i][1]))
    theta.append(acos(inner_product(v[0], v[1]) / (length(v[0]) * length(v[1]))))
radius = length((p[1][0] - p[0][0], p[1][1] - p[0][1])) / 2 / sin(theta[2])
theta.sort()
for n in range(1, 51):
    s = theta[0] / n
    for i in [1, 2]:
        f = fmod(theta[i], s)
        if f > 1e-5 and f + 1e-5 < s:
            break
    else:
        break
print '%.8lf' % (radius ** 2 * sin(theta[0] * 2 / n) / 2 * (2 * pi / (theta[0] * 2 / n)))
