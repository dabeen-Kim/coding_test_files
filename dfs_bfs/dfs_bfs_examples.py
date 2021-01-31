#'음료수 얼려 먹기' 문제(dfs)
n, m = map(int, input().split())
tray = []

for _ in range(n):
    tray.append(list(map(int, input())))

def dfs(tray, pos):
    x, y = pos
    if tray[x][y] == 1:
        return 0

    tray[x][y] = 1
    plist = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    for p in plist:
        if 0 <= p[0] < n and 0 <= p[1] < m:
            dfs(tray, p)
    
    return 1

cnt = 0
for i in range(n):
    for j in range(m):
        cnt += dfs(tray, (i,j))

print(cnt)

--------------------------------------------------------------

#'미로 탈출' 문제(bfs)
from collections import deque

n,m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        px,py = queue.popleft()
        plist = [(px+1,py), (px,py+1), (px-1,py), (px,py-1)]

        for p in plist:
            if 0 <= p[0] < n and 0 <= p[1] < m and maze[p[0]][p[1]] == 1:
                maze[p[0]][p[1]] = maze[px][py] + 1
                queue.append(p)
    
    return maze[n-1][m-1]

print(bfs(0,0))
