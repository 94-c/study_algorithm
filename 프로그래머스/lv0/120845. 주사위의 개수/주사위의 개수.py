def solution(box, n):
    # 주어진 box 리스트의 각 요소에 // n 연산을 적용하여 새로운 리스트 생성
    answer = list(map(lambda x: x // n, box))
    
    # 새로운 리스트의 모든 요소를 곱하여 최종 결과 
    results = 1
    for result in answer:
        results *= result
    
    return results