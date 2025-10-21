s = input()

aNum = s.count('a')

bN = s[:aNum].count('b')
result = bN

for start in range(1, len(s)):
    end = (start + aNum - 1) % len(s)

    if s[start - 1] == 'b': bN -= 1
    if s[end] == 'b': bN += 1

    result = min(bN, result)

print(result)