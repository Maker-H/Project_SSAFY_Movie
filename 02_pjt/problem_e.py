import requests
from pprint import pprint


def credits(title):
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
    
    credits_path = f'/movie/{id}/credits'
    credits_params = {
    'api_key' : '5bacb04d2b05e092546e27ae66aa1c69',
    'language' : 'ko-Kr',
    } 
    credits_response = requests.get(BASE_URL + credits_path, params=credits_params).json()
    credits_casts = credits_response.get('cast')

    cast = []
    directing = []
    for credits_cast in credits_casts:
        if credits_cast.get('cast_id') < 10:
            cast.append(credits_cast.get('name'))

    credits_crews = credits_response.get('crew')
    for credits_crew in credits_crews:
        crew_name = credits_crew.get('name')
        crew_department = credits_crew.get('department') 
        if  crew_department == 'Directing' and crew_name not in directing:
            directing.append(crew_name)
   
    return {'cast':cast, 'directing': directing}
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
