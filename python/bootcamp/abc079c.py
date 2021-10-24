
def reOp(s, i, f, sum):
    if i == 3:
        if sum == 7:
            print(f + '=7')
            exit()
    
    else:
        reOp(s, i + 1, f + '+' + s[i + 1], sum + int(s[i + 1]))
        reOp(s, i + 1, f + '-' + s[i + 1], sum - int(s[i + 1]))

s = input()
reOp(s, 0, s[0], int(s[0]))