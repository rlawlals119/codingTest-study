n, m = map(int, input().split())

nums = list(set(list(map(int, input().split()))))
nums.sort()

def DFS(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    for n in nums:
        if len(seq) == 0: DFS([n])
        elif seq[-1] <= n:
            DFS(seq + [n])

DFS([])