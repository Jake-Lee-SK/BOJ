import sys
sys.stdin = open('input.txt')

N = int(input())
matrix = []
numbers = list(map(int, input().split()))
for i in range(N):
    a = numbers[i]
    matrix.append([i+1, a])
matrix.sort(key=lambda x : x[1])
cnt = 0
for i in range(N):
    for j in range(0, i+1):
        cnt += matrix[j][1]
print(cnt)