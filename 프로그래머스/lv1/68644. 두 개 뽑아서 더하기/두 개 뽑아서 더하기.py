def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
            
    return sorted(list(set(answer)))

#from itertools import combinations
#def solution(numbers):
    #answer = set()
    #for i in combinations(numbers, 2):
        #answer.add(i[0] + i[1])
        #answer.add(sum(i))    
    #return sorted(list(answer))