A = '12ab112ab2ab'
B = '12ab'

stack = []
for i in range(len(A)):
    stack.append(A[i])
    if ''.join(stack[-len(B):]) == B:
        del stack[-len(B):]
A = ''.join(stack)

if A == '':
    print('FRULA')
else:
    print(A)