txt = tuple(input()) 
n = "N" in txt
s = "S" in txt 
e = "E" in txt 
w = "W" in txt 

flag = True
# 北、南どちらかしかないとき
if not (n and s): flag = False
# 東、西どちらかしかないとき
if not (e and w): flag = False
# 北、南があり、東、西がないとき
if (n and s) and (not e and not w): flag = True
# 東、西があり、北、南がないとき
if (e and w) and (not n and not s): flag = True

if flag:
    print("Yes")
else:
    print("No")




