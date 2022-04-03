N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
elif N>2:
    a = 1
    b = 2
    check = 0
    while check != N-1:
        c = a+b
        a = b
        b = c
        check += 1
print(a%10007)