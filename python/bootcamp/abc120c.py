from collections import Counter
s = input().rstrip()
s0 = s.count('0')
s1 = s.count('1')
print(min(s0, s1) * 2)