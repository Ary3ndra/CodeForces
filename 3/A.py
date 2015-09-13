from sys import stdout
s = raw_input()
t = raw_input()
s = [ord(s[0]) - ord('a'), int(s[1]) - 1]
t = [ord(t[0]) - ord('a'), int(t[1]) - 1]
print max(abs(s[0] - t[0]), abs(s[1] - t[1]))
while s != t:
    if s[0] < t[0]:
        stdout.write('R')
        s[0] += 1
    elif s[0] > t[0]:
        stdout.write('L')
        s[0] -= 1
    if s[1] < t[1]:
        stdout.write('U')
        s[1] += 1
    elif s[1] > t[1]:
        stdout.write('D')
        s[1] -= 1
    stdout.write('\n')
