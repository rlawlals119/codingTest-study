n, d, k, c = map(int, input().split())

sushis = []
for _ in range(n):
    sushis.append(int(input()))

count = [0 for _ in range(d + 1)]
for i in range(k):
    count[sushis[i]] += 1
count[c] += 1

s = set(sushis[:k])
s.add(c)
ans = len(s)
for i in range(1, n):
    end = (i + k - 1) % n
    count[sushis[i - 1]] -= 1
    if count[sushis[i - 1]] == 0: s.discard(sushis[i - 1])
    count[sushis[end]] += 1
    s.add(sushis[end])
    ans = max(ans, len(s))
 
print(ans)