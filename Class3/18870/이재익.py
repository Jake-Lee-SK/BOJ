import sys
sys.stdin = open('input.txt')

N = int(input())
functions = list(map(int, input().split()))
sorted_functions = sorted(set(functions))
dictionary = {}
for i in range(len(sorted_functions)):
    dictionary[sorted_functions[i]] = i
for i in range(N):
    print(dictionary[functions[i]])