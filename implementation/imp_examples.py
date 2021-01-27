#상하좌우 문제
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

#시간 문제
N = int(input())
result = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)

