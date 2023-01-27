import requests
from pprint import pprint

def popular_count():
    #https://api.themoviedb.org/3/movie/popular?api_key=5bacb04d2b05e092546e27ae66aa1c69&language=ko&page=1&region=Kr
    
    # 1. url 정보 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '5bacb04d2b05e092546e27ae66aa1c69',
        'language' : ' ko',
        'region' : 'Kr',
    } # page는 디폴트라 넣지않는다.
    
    # 2. 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    results = response.get('results')
    
    # 3. 결과  
    return len(results)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
