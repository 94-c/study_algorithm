def solution(genres, plays):
    answer = []
    
    # 장르별 total play를 저장하는 딕셔너리
    total = {}
    
    # 장르별 play 수를 저장하는 딕셔너리
    play = {}
    
    for i in range(len(genres)):
        # 딕셔너리안에 key가 존재하면 플러스, 없으면 초기화
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]
        
        # 장르별 play 수 딕셔너리안에 key가 존자하면 플러스, 없으면 초기화
        if genres[i] in play:
            play[genres[i]].append([plays[i], i])
        else:
            play[genres[i]] = [[plays[i], i]]
            
    rank = sorted(total, key=total.get, reverse=True)
    
    for x in rank:
        play_rank = sorted(play[x], key=lambda x: (-x[0], x[1]))
        
        if len(play_rank) == 1:
            answer.append(play_rank[0][1])
        else:
            for i in range(2):
                answer.append(play_rank[i][1])
    
    return answer