def solution(n, k):
    beverages = n // 10
    answer = 12000 * n + 2000 * (k - beverages)
    return answer