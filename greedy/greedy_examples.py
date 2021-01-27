#'큰 수의 법칙' 문제
N, M, K = map(int, input().split())
numlist = list(map(int, input().split()))

numlist.sort(reverse=True)
pattern = numlist[0]*K + numlist[1]
times = M // (K+1)
remain = M % (K+1)

result = pattern*times + numlist[0]*remain

print(result)

#'숫자 카드 게임' 문제
N, M = map(int, input().split())
cards = [[0]*M for _ in range(N)]
result = []

for i in range(N):
    cards[i] = list(map(int, input().split()))
    result.append(min(cards[i]))

print(max(result))

#'1이 될 때까지' 문제
N, K = map(int, input().split())
result = 0

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    
    result += 1

print(result)
