def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)
p = (6 - max(map(int, raw_input().split())) + 1, 6)
gcd = GCD(*p)
print '%d/%d' % (p[0] / gcd, p[1] / gcd)
