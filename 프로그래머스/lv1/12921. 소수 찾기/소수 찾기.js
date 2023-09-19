function solution(n) {
  const arr = Array(n+1).fill(true);
    
  arr[0] = arr[1] = false;
  
  for(let i=2; i*i <= n; i++) {
      for(let j=i*2; j<=n; j += i) {
          arr[j] = false;
      }
  }
  return arr.filter(v => v).length  
}