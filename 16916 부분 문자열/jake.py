
# 테이블 만드는 함수
def table_make(pattern):
    # 패턴 길이만큼의 빈 테이블을 생성
    table = [0 for _ in range(len(pattern))]
    # 시작 번호를 지정
    j = 0
    # 끝 번호는 계속 증가
    for i in range(1, len(pattern)):
        print(i, j, table)
        # j가 0보다 크고, 인덱스가 지정해 도출된 것이 서로 맞지 않을 때
        while j>0 and pattern[i] != pattern[j]:
            # 테이블에 저장된 j-1번째 수로 되돌아감
            j = table[j-1]
        # 패턴에서 접두사와 접미사가 같다면
        if pattern[i] == pattern[j]:
            # j를 옮김
            j += 1
            # table에 j를 저장
            table[i] = j
    return table
# 찾는 함수
def find(pattern, txt):
    table = table_make(pattern)
    j = 0
    for i in range(len(txt)):
        while j > 0 and txt[i] != pattern[j]:
            j = table[j-1]
        if txt[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

text = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxabcabcabdabcabcabdabcabcabdabcabcabe'
pattern = 'abcabcabdabcabcabdabcabcabe'

if find(pattern, text):
    print(1)
else:
    print(0)