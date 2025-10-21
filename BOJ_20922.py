n, k = map(int, input().split())

seq = list(map(int, input().split()))
dic = {}

for s in seq:
    if not s in dic: dic[s] = 0

start = 0
end = 0
cnt = 0
result = 0
while (end < n):
    if dic[seq[end]] < k:
        dic[seq[end]] += 1
        end += 1
        cnt += 1
        result = max(result, cnt)
    else:
        dic[seq[start]] -= 1
        start += 1
        cnt -= 1
        

print(result)