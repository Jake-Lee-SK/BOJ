import sys
sys.stdin = open('input.txt')

# 정리하자면,
# 1. 괄호가 껴있을 경우에는 우선 괄호를 넣어준다.
# 그리고 괄호 다음에 있는 숫자는 숫자 식으로 계속 넣어주고
# 연산자만 따로 정리한다.
# 이후 닫는 괄호가 나오면, 여는 괄호~닫는 괄호 사이의 모든 연산자를 식에 넣는다.
# 2. 그 외 괄호가 없다면(혹은 괄호 안에서의)
# 연산자 리스트가 비어있다면 우선순위 상관없이 연산자를 추가한다.
# 새로운 연산자가 들어올 경우 우선순위를 따진다.
# 높으면 : 연산자 리스트에 바로 추가한다.
# 같으면 : 식에다가 마지막 연산자를 넣고, 새로운 연산자로 대체한다.
# 낮으면 : 마지막 연산자를 빼서 식에다 추가, 이후 맨 뒤 연산자의 우선순위가 새로운 연산자의 우선순위와 같거나 클때까지
# 식에다 연산자를 추가한다.
# 이후 새로운 연산자가 맨 뒤 연산자보다 같거나 작다면 연산자 리스트에 추가한다.
# 숫자나 글자는 곧바로 식에다 추가한다.
# 이후 남아있는 연산자 리스트를 싹 비운다.
# 출력한다.

M = input()  # 후위표기식으로 변경하고 싶은 중위표기식

rank = {'(': 0, '+': 1, '-': 1, '/': 2, '*': 2}  # 우선순위를 지정
operator = []  # 연산자
sic = []  # 최종도출되는 후위표기식
for i in range(len(M)):
    print(sic)
    print(operator)
    if M[i] == '(':  # 괄호면 우선 연산자 리스트에 추가함
        operator.append(M[i])
    elif M[i] == ')':  # 닫는 괄호면 그때까지 추가된 모든 연산자를 최종식에 추가
        while operator[-1] != '(':
            sic.append(operator.pop())
        operator.pop()  # 여는 괄호를 삭제
    elif M[i] in '+*-/':  # 다음 것이 연산자라면
        if len(operator) == 0:  # 연산자 안에 아무것도 없을 때에는
            operator.append(M[i])  # 연산자 리스트에 연산자를 추가
        else:  # 무언가 있을 때에는
            if rank[M[i]] == rank[operator[-1]]:  # 새로운 것이 마지막에 있는 연산자와 우선순위가 같을 때
                sic.append(operator.pop())  # 식에다가 마지막 연산자를 추가함
                operator.append(M[i])  # 그리고 다시 연산자를 바꿔줌
            elif rank[M[i]] > rank[operator[-1]]:  # 새로운 것이 마지막 연산자보다 우선순위가 높을 때
                operator.append(M[i])  # 연산자 리스트에 바로 추가만 해줌
            elif rank[M[i]] < rank[operator[-1]]:  # 우선순위가 낮을 때
                sic.append(operator.pop())  # 마지막 연산자를 빼서 식에다 추가해줌
                while len(operator) > 0 and rank[M[i]] <= rank[operator[-1]]:  # 오퍼레이터 연산자 길이가 0이 될 때까지
                    # 그리고 맨 뒤 연산자 랭크가 새로운 것보다 같거나 클 때까지
                    sic.append(operator.pop())  # 연산자 리스트 안에 있는 모든 것을 식에다 추가함
                operator.append(M[i])  # 그후 연산자 리스트에 추가함
    else:
        sic.append(M[i])  # 숫자라면 식에다 그냥 바로 추가함.

while len(operator) > 0:
    sic.append(operator.pop())  # 다 끝난 후에 남아있는 것들 모두 추가함.

print(''.join(sic))