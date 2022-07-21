import sys
sys.stdin = open('input.txt')

def Foward(roboto, direction, times):
    global robot
    global A, B
    global N, M
    if times == 0:
        return
    # 동쪽을 바라볼 때
    if direction == 'E':
        # y축을 하나씩 더하면서 이동
        # 벽 위치를 넘어가면 벽과 충돌
        if robot[roboto][1]+1 > B:
            return error.append(f'Robot {roboto} crashed into the wall')
        elif [robot[roboto][0], robot[roboto][1]+1] in robot:
            for i in range(N):
                if robot[i] == [robot[roboto][0], robot[roboto][1]+1]:
                    return error.append(f'Robot {roboto} crashed into robot {i}')
        else:
            robot[roboto][1] += 1
            Foward(roboto, direction, times-1)
    # 서쪽을 바라볼 때
    elif direction == 'W':
        #
        if direction == 'E':
            if robot[roboto][1] - 1 > A:
                return error.append(f'Robot {roboto} crashed into the wall')
            elif [robot[roboto][0], robot[roboto][1]-1] in robot:
                for i in range(N):
                    if robot[i] == [robot[roboto][0], robot[roboto][1]-1]:
                        return error.append(f'Robot {roboto} crashed into robot {i}')
        else:
            robot[roboto][1] -= 1
            Foward(roboto, direction, times - 1)
    # 남쪽을 바라볼 때
    elif direction == 'S':
        if robot[roboto][0] - 1 > A:
            return error.append(f'Robot {roboto} crashed into the wall')
        elif [robot[roboto][0] - 1, robot[roboto][1]] in robot:
            for i in range(N):
                if robot[i] == [robot[roboto][0] - 1, robot[roboto][1]]:
                    return error.append(f'Robot {roboto} crashed into robot {i}')
        else:
            robot[roboto][0] -= 1
            Foward(roboto, direction, times - 1)
    # 북쪽을 바라볼 때
    elif direction == 'N':
        if robot[roboto][0] + 1 > A:
            return error.append(f'Robot {roboto} crashed into the wall')
        elif [robot[roboto][0]+1, robot[roboto][1]] in robot:
            for i in range(N):
                if robot[i] == [robot[roboto][0]+1, robot[roboto][1]]:
                    return error.append(f'Robot {roboto} crashed into robot {i}')
        else:
            robot[roboto][0] += 1
            Foward(roboto, direction, times - 1)
# 땅의 크기
A, B = map(int, input().split())
N, M = map(int, input().split())
robot = []
robot.append([])
robot_directions = []
robot_directions.append('0')
error = []
for roboto in range(N):
    x, y, direction = input().split()
    robot.append([int(x), int(y)])
    robot_directions.append(direction)
for order in range(M):
    order_robot, order_sort, times = input().split()
print(robot, robot_directions)
