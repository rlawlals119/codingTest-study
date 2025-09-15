a, b, c = map(int, input().split())

def mod_pow(a, b, c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = mod_pow(a, b // 2, c)
        return half * half % c
    else:
        return (a * mod_pow(a, b - 1, c)) % c
print(mod_pow(a, b, c))