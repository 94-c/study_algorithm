def solution(my_string):
    answer = []
    
    for i in list(my_string):
        # isnumeric() : 주어진 문자열이 숫자로 되어있는지 검사하는 함수
        if i.isnumeric():
            answer.append(int(i))
        
    return sorted(answer)