from collections import deque
n, k = map(int, input().split())

q = list(map(int, input().split()))

belt = [False for _ in range(n - 1)]

cnt = 0
result = 0
while (cnt < k):
    result += 1
    # 회전
    belt.pop()
    q.insert(0, q.pop())

    belt.insert(0, False)

    # 로봇 한칸씩 옮기기
    for i in range(n - 2, 0, -1):
        if belt[i] and q[i + 1] != 0 and (i == n - 2 or not belt[i + 1]):
            belt[i] = False
            q[i + 1] -= 1
            if q[i + 1] == 0: cnt += 1
            if i + 1 < n - 1:
                belt[i + 1] = True
    
    if q[0] != 0:
        belt[0] = True
        q[0] -= 1
        if q[0] == 0: cnt += 1

print(result)