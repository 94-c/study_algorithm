def solution(my_string, num1, num2):
    # 빈 문자열을 초기화합니다.
    answer = ''
    
    # 문자열을 리스트로 변환합니다. (문자열은 불변(immutable)이지만 리스트는 변경 가능(mutable)하므로 교체가 가능합니다.)
    my_string = list(my_string)
    
    # 주어진 두 인덱스(num1, num2)의 문자를 교체하기 위해 임시(tmp) 변수에 첫 번째 인덱스(num1)의 문자를 저장합니다.
    tmp = my_string[num1]
    
    # 두 번째 인덱스(num2)의 문자를 첫 번째 인덱스(num1)에 저장합니다.
    my_string[num1] = my_string[num2]
    
    # 임시(tmp) 변수에 저장된 문자를 두 번째 인덱스(num2)에 저장합니다.
    my_string[num2] = tmp
    
    # 교체된 문자열 리스트를 다시 문자열로 변환합니다.
    answer = ''.join(my_string)
    
    # 교체된 문자열을 반환합니다.
    return answer