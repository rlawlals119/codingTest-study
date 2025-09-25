t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(1)
        continue
    print(pow(2, n - 2, 10 ** 9 + 7))