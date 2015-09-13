keypad = []
for i in range(3):
    keypad.append(raw_input())
if keypad[0][0] == keypad[2][2] and keypad[0][1] == keypad[2][1] and keypad[0][2] == keypad[2][0] and keypad[1][0] == keypad[1][2]:
    print 'YES'
else:
    print 'NO'
