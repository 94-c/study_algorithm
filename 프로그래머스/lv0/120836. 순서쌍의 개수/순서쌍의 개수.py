def solution(n):
    answer = []
    # 1부터 n까지의 숫자를 하나씩 순회합니다.
    for i in range(1, n + 1):
        # 만약 n을 i로 나눈 나머지가 0이라면, i는 n의 약수입니다.
        if n % i == 0:
            # (i, n // i) 형태의 튜플을 리스트에 추가합니다.
            answer.extend([(i, n // i)])
    
    # 약수 쌍의 개수, 즉 리스트의 길이를 반환합니다.
    return len(answer)