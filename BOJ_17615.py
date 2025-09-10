n = int(input())

ball = input()

ball_set = set(ball)

def solution():
    if len(ball_set) == 1: return 0
    bCnt = ball.count('B')
    rCnt = ball.count('R')

    ans = 500001

    first_color = ball[0]
    first_ball = 1
    last_color = ball[-1]
    last_ball = 1
    for i in range(1, n):
        if ball[i] == first_color:
            first_ball += 1
        else: break
    for i in range(n - 2, 0, -1):
        if ball[i] == last_color:
            last_ball += 1
        else: break
    if first_color == 'B': ans = min(ans, bCnt - first_ball, rCnt)
    else: ans = min(ans, rCnt - first_ball, bCnt)
    
    if last_color == 'B': ans =  min(ans, bCnt - last_ball, rCnt)
    else: ans = min(ans, rCnt - last_ball, bCnt)

    return ans

print(solution())