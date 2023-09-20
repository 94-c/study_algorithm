function solution(left, right) {
    var answer = 0;
    
    // left부터 right까지의 약수 개수 구하기
    for(let i = left; i<=right; i++) {
        // 약수의 개수를 저장
        let count = i**0.5;
        
        if(Number.isInteger(count)) {
            answer -= i;
        } else {
            answer += i;
        }
    }
    return answer;
}
