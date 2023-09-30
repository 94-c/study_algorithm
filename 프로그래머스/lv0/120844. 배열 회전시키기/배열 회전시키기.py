def solution(numbers, direction):
    return [numbers.pop()] + numbers if direction=='right' else numbers + [numbers.pop(0)]