from collections import deque

n, k = map(int, input().split())

if k <= n:
    print(n - k)

else:
    visited = [100001 for _ in range(100002)]
    q = deque([(k, 0)])
    visited[k] = 0

    while(q):
        loc, cnt = q.popleft()
        if loc == n:
            print(cnt)
            break

        if loc % 2 == 0 and visited[loc // 2] > cnt:
            visited[loc // 2] = cnt
            q.appendleft((loc // 2, cnt))
        if loc - 1 >= 0 and visited[loc - 1] > cnt + 1:
            visited[loc - 1] = cnt + 1
            q.append((loc - 1, cnt + 1))
        if loc + 1 <= 100000 and visited[loc + 1] > cnt + 1:
            visited[loc + 1] = cnt + 1
            q.append((loc + 1, cnt + 1))
        