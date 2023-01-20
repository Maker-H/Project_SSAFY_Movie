import json


def dec_movies(movies):
    release_dec_movies = []
    for one_ele_movie in movies:
        movie_id = one_ele_movie.get('id')
        movie_file_name = f'data/movies/{movie_id}.json'
        movie_json = open(movie_file_name, encoding='utf-8')
        movie_list = json.load(movie_json)

        if movie_list.get('release_date')[5:7] == '12': 
            release_dec_movies.append(movie_list.get('title'))

    return release_dec_movies        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
