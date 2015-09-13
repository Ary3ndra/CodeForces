inroom = {}
traffic = 0
while True:
    try:
        s = raw_input()
    except EOFError:
        break
    if s[0] == '+':
        inroom[s[1:]] = None
    elif s[0] == '-':
        inroom.pop(s[1:])
    else:
        traffic += len(s.split(':')[1]) * len(inroom)
print traffic
