import string

a, b = map(int, input().split())
s = input()
aa = ""
bb = ""

def no():
    print("No")
    exit()

if (a + b + 1) != len(s) \
    or s[a] != "-":
    no()

aa = s[:a]
bb = s[a + 1:]
if len(aa) != a or len(bb) != b: no()

for v in iter(aa):
    if v not in string.digits: no()

for v in iter(bb):
    if v not in string.digits: no()


print("Yes")



