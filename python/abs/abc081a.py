from sys import stdin

s = stdin.readline().rstrip()
count = 0
for i in range(3):
    if(s[i] == '1'):
        count += 1

print(count)
