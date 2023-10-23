def solution(numbers):
    nums = ['zero','one','two','three','four','five', 'six','seven','eight','nine']
    # enumerate() : nums에 있는 문자열과 인덱스를 함께 불러오는 방법
    for i,n in enumerate(nums):
        numbers = numbers.replace(n, str(i))
        
    answer = int(numbers)
    return answer