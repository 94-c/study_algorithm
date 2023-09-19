def solution(sides):
    sides.sort()
    
    answer = 1
    return answer if sides[2] < sides[0] + sides[1] else 2