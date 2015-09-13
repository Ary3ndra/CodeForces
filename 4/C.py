n = input()
d = dict()
for _ in range(n):
    name = raw_input()
    if name not in d:
        print 'OK'
        d[name] = 1
    else:
        d[name + `d[name]`] = 1
        print name + `d[name]`
        d[name] += 1
