def solution(dots):
    weight = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    
    return weight * height