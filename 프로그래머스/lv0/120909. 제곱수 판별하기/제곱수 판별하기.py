def solution(n):
    ## 0.5를 제곱 하면 n의 제곱근이 float 형태로 반환
    if int(n ** 0.5) ** 2 == n:
        return 1
    else:
        return 2
    