S = 'abababababababa'
a = S.count('a')

ans = len(S)
# 앞에서부터 체크할 때(0~len(S)-a)
for i in range(a - 1, len(S)):
    ans = min(ans, S[i - a + 1:i + 1].count('b'))
# 끊어져있는 부분을 이어서 체크한다고 생각할 때
for i in range(0, a - 1):
    ans = min(ans, (S[i - a + 1:] + S[:i + 1]).count('b'))

print(ans)

