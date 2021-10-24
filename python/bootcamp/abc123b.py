A = list(int(input()) for _ in range(5))
B = [ a - a % 10 + 10 if a % 10 != 0 else a for a in A]
diff = [(b - a) for a, b in zip(A, B)]
print(sum(B) - max(diff))

