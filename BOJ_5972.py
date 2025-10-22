from queue import PriorityQueue
import math
n, m = map(int, input().split())

graph = [[] for __ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [math.inf for _ in range(n + 1)]

q = PriorityQueue()
q.put((0, 1))
visited[0] = 0
visited[1] = 0

while(not q.empty()):
    v, loc = q.get()
    if loc == n:
        print(v)
        break
    for next, w in graph[loc]:
        if v + w < visited[next]:
            q.put((v + w, next))
            visited[next] = v + w