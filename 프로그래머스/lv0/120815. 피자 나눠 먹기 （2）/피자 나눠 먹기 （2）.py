def solution(n):
    tmp = 6 / n
    
    for i in range(1, 101):
        if (tmp * i).is_integer():
            answer = i
            break
            
    return answer