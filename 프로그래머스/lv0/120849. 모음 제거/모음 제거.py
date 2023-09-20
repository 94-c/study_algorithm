def solution(my_string):
    answer = ''
    
    word = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i in word:
            continue
        else:
            answer += i
            
    return answer