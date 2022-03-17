import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
Coins = [int(input()) for i in range(N)]
count = 0
while 1:
    use_coin = 0
    for Coin in Coins:
        if Coin <= K:
            use_coin = Coin
    if K == 0:
        break
    else:
        K = K - use_coin
        count += 1

print(count)