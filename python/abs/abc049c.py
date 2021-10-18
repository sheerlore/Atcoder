s = input()
s = s.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
print("YES" if len(s) == 0 else "NO")