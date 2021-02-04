#'1로 만들기' 문제
x = int(input())
array = [0] * x

for i in range(2,x+1):
    candidate = []

    if i % 5 == 0:
        candidate.append(array[i//5-1]+1)
    if i % 3 == 0:
        candidate.append(array[i//3-1]+1)
    if i % 2 == 0:
        candidate.append(array[i//2-1]+1)

    candidate.append(array[(i-1)-1]+1)

    array[i-1] = min(candidate)

print(array[x-1])

-----------------------------------------------------------------

#'개미 전사' 문제
n = int(input())
foods = list(map(int, input().split()))

dptable = [foods[0], foods[1]]
for i in range(2, n):
    dptable.append(max(dptable[i-2]+foods[i], dptable[i-1]))

print(dptable[n-1])

-----------------------------------------------------------------

#'바닥 공사' 문제
n = int(input())

dptable = [1,3]
for i in range(2,n):
    dptable.append((dptable[i-1] + 2*dptable[i-2]) % 796796)

print(dptable[n-1])

-------------------------------------------------------------------

#'효율적인 화폐 구성' 문제
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

array = [10001]*(m+1)
array[0] = 0


for coin in coins:
    for money in range(coin, m+1):
        array[money] = min(array[money], array[money - coin] + 1)


if array[m] == 10001:
    print(-1)
else:
    print(array[m])
