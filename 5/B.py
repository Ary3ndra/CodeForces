from sys import stdin, stdout
lines = stdin.readlines()
width = max(len(x) for x in lines) - 1
stdout.write('*' * (width + 2) + '\n')
alignleft = True
for line in lines:
    line = line[:-1]
    stdout.write('*')
    if (width + len(line)) % 2 != 0:
        if alignleft:
            stdout.write(' ' * ((width - len(line)) / 2))
            stdout.write(line)
            stdout.write(' ' * ((width - len(line)) / 2 + 1))
        else:
            stdout.write(' ' * ((width - len(line)) / 2 + 1))
            stdout.write(line)
            stdout.write(' ' * ((width - len(line)) / 2))
        alignleft = not alignleft
    else:
        stdout.write(' ' * ((width - len(line)) / 2))
        stdout.write(line)
        stdout.write(' ' * ((width - len(line)) / 2))
    stdout.write('*\n')
stdout.write('*' * (width + 2) + '\n')
