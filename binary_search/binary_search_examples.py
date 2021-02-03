#'부품 찾기' 문제
n = int(input())
parts = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))
parts.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    
    return False

for part in checklist:
    if binary_search(parts, part, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()

-----------------------------------------------------------------------

'떡볶이 떡 만들기' 문제
n, m = map(int, input().split())
heights = list(map(int, input().split()))

end = max(heights)
start = 0
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2

    for h in heights:
        if h > mid:
            total += h-mid
    
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1


print(result)
