def solution(genres, plays):
    answer = []
    
    # 1. 데이터 집계 (O(N))
    # 장르별 총 재생 수
    genres_total_plays = {}  # 예: {"pop": 3100, "classic": 1450}
    # 장르별 곡 리스트 (재생수 내림차순, 인덱스 오름차순 정렬을 위해 튜플 저장)
    genres_songs = {}        # 예: {"pop": [(-600, 1), (-2500, 4)], ...}

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        # 딕셔너리 초기화
        if g not in genres_total_plays:
            genres_total_plays[g] = 0
            genres_songs[g] = []
            
        # 총 재생수 누적
        genres_total_plays[g] += p
        
        # (재생수 내림차순, 인덱스 오름차순) 정렬을 위한 트릭
        # (-재생수, 인덱스) 튜플로 저장
        genres_songs[g].append((-p, i))

    # 2. 장르 정렬 (O(K log K))
    # 총 재생수(item[1])를 기준으로 장르를 내림차순 정렬
    sorted_genres = sorted(genres_total_plays.items(), key=lambda item: item[1], reverse=True)

    # 3. 장르별 곡 정렬 및 Top 2 추출 ( K * O(Ng log Ng) )
    for g_tuple in sorted_genres:
        g = g_tuple[0]  # 장르 이름 (예: "pop")
        
        # 해당 장르의 곡 리스트를 정렬
        # (-p, i) 튜플이므로, -p 오름차순 (p 내림차순) 정렬이 되고,
        # -p가 같으면 i 오름차순 (인덱스) 정렬이 됨
        songs_in_genre = sorted(genres_songs[g])
        
        # Top 2 추출 (장르에 곡이 1개일 수도 있으므로 min 사용)
        for k in range(min(len(songs_in_genre), 2)):
            song_index = songs_in_genre[k][1] # (음수 재생수, *인덱스*)
            answer.append(song_index)
            
    return answer