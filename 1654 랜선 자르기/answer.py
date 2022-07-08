import sys
sys.stdin = open('input.txt')
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함
K, N = map(int, input().split())
numbers = list(int(input()) for _ in range(K))
if N == 1:
    print(max(numbers))
else:
    left, right = 1, max(numbers)
    while left<=right:
        mid = (left+right)//2
        total = 0
        for i in numbers:
            total += (i//mid)
        if total >= N:
            left = mid + 1
        else:
            right = mid - 1
    print(right)