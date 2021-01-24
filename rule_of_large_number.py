N, M, K = map(int, input().split())
numlist = list(map(int, input().split()))

numlist.sort(reverse=True)
pattern = numlist[0]*K + numlist[1]
times = M // (K+1)
remain = M % (K+1)

result = pattern*times + numlist[0]*remain

print(result)