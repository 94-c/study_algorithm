function solution(arr)
{
    var answer = [];

    for(var i=0; i<arr.length; i++) {
        //중복확인
        if(arr[i] !== arr[i+1]) {
            //중복 되지 않은 요소 추가
            answer.push(arr[i]);
        }
    }
    return answer;
}