n = int(input())
s = input().rstrip()

x = 0
maxx = 0 
for i in range(n):
    if s[i] == "I": x += 1
    if s[i] == "D": x -= 1

    if maxx <= x: maxx = x

print(maxx)
