#function solution(arr)
#{
#    var answer = [];
#
#    for(var i=0; i<arr.length; i++) {
#        //중복확인
#        if(arr[i] !== arr[i+1]) {
#           //중복 되지 않은 요소 추가
#            answer.push(arr[i]);
#        }
#    }
#    return answer;
#}

def solution(arr):
    # 결과를 저장할 빈 리스트를 생성
    answer = []
    
    # 입력 리스트(arr)를 순회하면서 중복된 요소를 제거
    for i in arr:
        # answer[-1:]: 이것은 리스트 answer의 마지막 요소를 슬라이싱하는 부분
        if answer[-1:] == [i]:
            # 중복 요소이므로 다음 요소로 넘어감
            continue
        # 중복되지 않는 경우, 현재 요소(i)를 answer 리스트에 추가
        answer.append(i)
    
    # 중복을 제거한 결과를 반환
    return answer