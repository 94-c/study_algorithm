def solution(numbers):
    numbers.sort()
    #처음에 numbers 배열을 정렬해서, max 함수를 써서 1번째 요소와 2번째 요소가 음수일 경우에 곱한 값과, 마지막 요소와 마지막에서 2번째 요소를 곱한 값을 비교해서 더 큰 값을 구함
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])