w = input()
count = {}
for c in iter(w):
    if c not in count.keys(): count[c] = 0
    count[c] += 1

flag = True
for n in count.values():
    if n % 2 != 0:
        flag = False

if flag: print("Yes")
else: print("No")
