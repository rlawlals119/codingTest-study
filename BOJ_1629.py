a, b, c = map(int, input().split())

num = a % c
if b == 1: print(num)
else:
    pattern = []
    for _ in range(b - 1):
        num = num * a % c
        if num in pattern: break
        pattern.append(num)

    if len(pattern) == 1: print(pattern[0])
    else: print(pattern[(b - 1) % len(pattern) - 1])