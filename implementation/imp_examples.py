#'상하좌우' 문제
N = int(input())
plans = input().split()
point = [1, 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
moves = ['U', 'D', 'L', 'R']

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
    
    if not (0 < nx <= N and 0 < ny <= N):
        continue

    point[0], point[1] = nx, ny 

print(point[0], point[1])

--------------------------------------------------------------

#'시간' 문제
N = int(input())
result = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)

--------------------------------------------------------------

#'왕실의 나이트' 문제
point = input()
columns = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
col , row = columns[point[0]], int(point[1])

moves = [[-2,1], [-2,-1], [2,1], [2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
count = 0

for move in moves:
    dcol = col + move[0]
    drow = row + move[1]

    if 0 < dcol < 9 and 0 < drow < 9:
        count += 1

print(count)

--------------------------------------------------------------

#'게임 개발' 문제
n, m = map(int, input().split())
Map = [[0]*m for _ in range(n)]
point = [0, 0]
point[0], point[1], d = map(int, input().split())
for i in range(n):
    Map[i] = list(map(int, input().split()))

def change(point, d):
    x = point[0]
    y = point[1]

    if d == 0:
        x -= 1
    elif d == 1:
        y += 1
    elif d == 2:
        x += 1
    else:
        y -= 1

    return [x,y]

stop = False
Map[point[0]][point[1]] = 2
count = 1
while not stop:
    turn_time = 0

    while True:
        if d == 0: d = 3
        else: d -= 1
        turn_time += 1

        dx, dy = change(point, d)
        if Map[dx][dy] == 0:
            point = change(point, d)
            Map[dx][dy] = 2
            count += 1
            break
        else:
            if turn_time == 4:
                point = change(point, (d+2)%4)
                if Map[point[0]][point[1]] == 1:
                    stop = True
                break
        
print(count)
