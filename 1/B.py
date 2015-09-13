import re
n = input()
for _ in range(n):
    s = raw_input()
    m = re.match(r'R(\d+)C(\d+)', s)
    if m is not None:
        r = int(m.group(1))
        c = int(m.group(2)) - 1
        cc = ''
        while c >= 0:
            cc = chr(c % 26 + ord('A')) + cc
            c = c / 26 - 1
        print '%s%d' % (cc, r)
    else:
        m = re.match(r'([A-Z]+)(\d+)', s)
        r = int(m.group(2))
        c = 0
        for i in m.group(1):
            c *= 26
            c += 1
            c += ord(i) - ord('A')
        print 'R%dC%d' % (r, c)
