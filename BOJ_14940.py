from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = [[-1 for _ in range(m)] for __ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: ans[i][j] = 0
        if graph[i][j] == 2:
            q = deque([(i, j, 0)])
            ans[i][j] = -1

            while q:
                x, y, dist = q.popleft()

                for a, b in direct:
                    dx = x + a
                    dy = y + b

                    if dx >= 0 and dx < n and dy >= 0 and dy < m and graph[dx][dy] != 0 and ans[dx][dy] == -1:
                        ans[dx][dy] = dist + 1
                        q.append((dx, dy, dist + 1))

            ans[i][j] = 0
for row in ans:
    print(*row)                 # 공백 구분으로 int도 바로 출력
