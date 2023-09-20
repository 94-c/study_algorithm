def solution(n):
    # 정수 n을 문자열로 변환하고, 문자열을 한 글자씩 나누어 리스트로 만듭니다.
    digits = [int(i) for i in str(n)]

    # 리스트 digits의 모든 원소를 더한 값을 반환합니다.
    return sum(digits)