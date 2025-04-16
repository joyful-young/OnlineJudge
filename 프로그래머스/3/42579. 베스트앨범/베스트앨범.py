def solution(genres, plays):
    N = len(genres)
    genre_play_cnt_and_songs = {}
    
    for i in range(N):
        if genres[i] in genre_play_cnt_and_songs:
            genre_play_cnt_and_songs[genres[i]][0] += plays[i]
            genre_play_cnt_and_songs[genres[i]][1].append(i)
        else:
            genre_play_cnt_and_songs[genres[i]] = [plays[i], [i]]
    
    # 장르별 재생 횟수 내림차순
    sorted_genre = list(genre_play_cnt_and_songs.keys())
    sorted_genre.sort(key=lambda x: -genre_play_cnt_and_songs[x][0])
        
    answer = []
    for genre in sorted_genre:
        if len(genre_play_cnt_and_songs[genre][1]) == 1:
            answer.append(genre_play_cnt_and_songs[genre][1][0])
        else:
            # 같은 장르 내 곡들을 재생 횟수 내림차순으로 정렬
            genre_play_cnt_and_songs[genre][1].sort(key=lambda x: -plays[x])
            answer.extend(genre_play_cnt_and_songs[genre][1][:2])
    return answer