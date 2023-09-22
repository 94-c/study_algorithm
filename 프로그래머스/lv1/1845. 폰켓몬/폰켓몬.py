def solution(nums):
    # nums 리스트의 고유한 원소 개수 구한다.
    answer = len(set(nums))
    
    # answer 보다 nums의 절반보다 크면,
    # nums의 길이의 절반을 반환합니다.
    if answer > len(nums) / 2:
        return len(nums) /2
    return answer