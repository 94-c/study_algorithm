def solution(dot):
    answer = 0
    
    if dot[0] > answer and dot[1] > answer:
        return 1
    elif dot[0] < answer and dot[1] > answer:
        return 2
    elif dot[0] < answer and dot[1] < answer:
        return 3
    elif dot[0] > answer and dot[1] < answer:
        return 4