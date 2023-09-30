def solution(order):
    clap_count = 0
    for digit in str(order):
        if digit in ['3', '6', '9']:
            clap_count += 1
    return clap_count