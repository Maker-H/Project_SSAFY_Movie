import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    search_path = '/search/movie'
    search_params = {
    'api_key' : '5bacb04d2b05e092546e27ae66aa1c69',
    'language' : 'ko-Kr',
    'query' : title,
    } 

    search_response = requests.get(BASE_URL + search_path, params=search_params).json()
    searched_movies = search_response.get('results')
    
    if not searched_movies:
        return None
    else:
        id = searched_movies[0].get('id')
    
    recommend_path = f'/movie/{id}/recommendations'
    recommend_params = {
    'api_key' : '5bacb04d2b05e092546e27ae66aa1c69',
    'language' : 'ko-Kr',
    } 
    recommend_response = requests.get(BASE_URL + recommend_path, params=recommend_params).json()
    recommend_movies = recommend_response.get('results')

    if not recommend_movies:
        return []
    
    recommend_movie_title = []
    for recommend_movie in recommend_movies:
        recommend_movie_title.append(recommend_movie.get('title'))

    return recommend_movie_title




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
