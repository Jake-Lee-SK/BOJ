def solution(s):
    answer = 0
    turn_count = 0
    s = list(s)
    while 1:
        check = []
        pop_check = 0
        if turn_count == len(s):
            break
        for i in s:
            if i == '[':
                check.append(0)
                pop_check += 1
            elif i == '{':
                check.append(1)
                pop_check += 1
            elif i == '(':
                check.append(2)
                pop_check += 1
            elif i == ']':
                pop_check -= 1
                if check and check[-1]==0:
                    check.pop()
            elif i == '}':
                pop_check -= 1
                if check and check[-1]==1:
                    check.pop()
            elif i == ')':
                pop_check -= 1
                if check and check[-1]==2:
                    check.pop()
            else:
                pass
        if len(check)==0 and pop_check == 0:
            answer += 1
        new = s.append(s.pop(0))
        turn_count += 1
    return answer
