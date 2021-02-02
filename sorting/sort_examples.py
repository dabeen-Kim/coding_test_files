'위에서 아래로' 문제
n = int(input())
array = []

for _ in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)

for i in range(n):
    print(array[i], end=' ')
print()

---------------------------------------------

'성적이 낮은 순서로 학생 출력하기' 문제
n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    array.append((name, score))

array.sort(key = lambda x: x[1])

for pair in array:
    print(pair[0], end=' ')
    
----------------------------------------------

'두 배열의 원소 교체' 문제
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

idx1 = 0
while k > 0:
    if a[idx1] >= b[idx1]:
        break
    else:
        a[idx1], b[idx1] = b[idx1], a[idx1]
        idx1 += 1
        k -= 1

print(sum(a))
