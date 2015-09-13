from sys import stdin
n = input()
m = [None] * n
dp2 = [[None] * n for x in range(n)]
dp5 = [[None] * n for x in range(n)]
zero = None
lines = stdin.readlines()
for i in range(n):
    m[i] = map(int, lines[i].split())
    for j in range(n):
        if m[i][j] == 0:
            m[i][j] = (18000, 18000)
            zero = (i, j)
        else:
            _2, _5 = 0, 0
            k = m[i][j]
            while k % 2 == 0:
                _2 += 1
                k /= 2
            while k % 5 == 0:
                _5 += 1
                k /= 5
            m[i][j] = (_2, _5)

    for j in range(n):
        if i == 0:
            if j == 0:
                dp2[i][j] = m[i][j][0]
                dp5[i][j] = m[i][j][1]
            else:
                dp2[i][j] = dp2[i][j - 1] + m[i][j][0]
                dp5[i][j] = dp5[i][j - 1] + m[i][j][1]
        else:
            if j == 0:
                dp2[i][j] = dp2[i - 1][j] + m[i][j][0]
                dp5[i][j] = dp5[i - 1][j] + m[i][j][1]
            else:
                u = dp2[i - 1][j] + m[i][j][0]
                d = dp2[i][j - 1] + m[i][j][0]
                if u < d:
                    dp2[i][j] = u
                else:
                    dp2[i][j] = d

                u = dp5[i - 1][j] + m[i][j][1]
                d = dp5[i][j - 1] + m[i][j][1]
                if u < d:
                    dp5[i][j] = u
                else:
                    dp5[i][j] = d

ans = ''
if dp2[-1][-1] > 1 and dp5[-1][-1] > 1 and zero:
    print 1
    print 'D' * zero[0] + 'R' * (n - 1) + 'D' * (n - zero[0] - 1)
else:
    if dp2[-1][-1] < dp5[-1][-1]:
        dp = dp2
    else:
        dp = dp5
    i, j = n - 1, n - 1
    while True:
        if i == 0:
            if j == 0:
                break
            else:
                j -= 1
                ans += 'R'
        else:
            if j == 0:
                i -= 1
                ans += 'D'
            else:
                if dp == dp2:
                    if dp[i - 1][j] + m[i][j][0] == dp[i][j]:
                        ans += 'D'
                        i -= 1
                    else:
                        ans += 'R'
                        j -= 1
                else:
                    if dp[i - 1][j] + m[i][j][1] == dp[i][j]:
                        ans += 'D'
                        i -= 1
                    else:
                        ans += 'R'
                        j -= 1
    print dp[-1][-1]
    print ans[::-1]
