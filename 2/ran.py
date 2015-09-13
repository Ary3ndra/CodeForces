import random
n = 1000
print n
for i in range(n):
    print ' '.join(`random.choice([2, 5])` for x in range(1000))
