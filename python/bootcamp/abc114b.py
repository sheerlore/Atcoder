
s = input().rstrip()

i = 0
ans = 10**10
while i <= len(s) - 2:
    n = int(s[i:i + 3])
    temp = abs(753 - n)
    if temp < ans:
        ans = temp
    i += 1

print(ans)
