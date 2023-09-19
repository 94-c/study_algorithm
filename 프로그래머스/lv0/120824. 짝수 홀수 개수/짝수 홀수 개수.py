def solution(num_list):
    ## 인덱스 0은 짝수 개수, 인덱스 1은 홀수 개수
    answer = [0, 0];
    for i in num_list:
        ## 현재 숫자를 2로 나눈 나머지를 구합니다. 짝수일 경우 0, 홀수일 경우 1이 됩니다.
        answer[i%2] += 1
    return answer