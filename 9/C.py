n = raw_input()
flag = False
res = 0
for x in n:
    res <<= 1
    if flag or x == '1':
        res += 1
    elif x != '0':
        flag = True
        res += 1
print res

