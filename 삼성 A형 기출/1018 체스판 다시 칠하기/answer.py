import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
matrix = [list(input()) for _ in range(A)]
ver1 = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
ver2 = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
# matrix 분할 or 그냥 return
if A == 8 and B == 8:
    count = 65
    check = 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] != ver1[i][j]:
                check += 1
    if check < count:
        count = check
    check = 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] != ver2[i][j]:
                check += 1
    if check < count:
        count = check
    print(count)
else:
    count = 65
    new_chess_board = [[] for _ in range(8)]
    for a in range(A-7):
        for b in range(B-7):
            new_chess_board = [row[b:b+8] for row in matrix[a:a+8]]
            check = 0
            for i in range(8):
                for j in range(8):
                        if new_chess_board[i][j] != ver1[i][j]:
                            check += 1
            if check < count:
                count = check

            check = 0
            for i in range(8):
                for j in range(8):
                        if new_chess_board[i][j] != ver2[i][j]:
                            check += 1

            if check < count:
                count = check
    print(count)