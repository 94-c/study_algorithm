def solution(score):
    answer = []
    list = []
    
    for i in score:
        list.append(sum(i)/len(i))
        
    sortArr = sorted(list, reverse=True)
    
    for i in list:
        answer.append(sortArr.index(i)+1)
        
    return answer