n = input()
record = []
score = {}
for i in range(n):
    s = raw_input().split()
    record.append((s[0], int(s[1])))
    score[s[0]] = score.get(s[0], 0) + int(s[1])
m = max(score[x] for x in score)
ties = [x for x in score if score[x] == m]
if len(ties) > 1:
    for i in score:
        score[i] = 0
    for r in record:
        score[r[0]] += r[1]
        if score[r[0]] >= m and r[0] in ties:
            print r[0]
            break
else:
    print ties[0]
