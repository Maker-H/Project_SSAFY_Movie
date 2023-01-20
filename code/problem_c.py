import json
from pprint import pprint


def movie_info(movies, genres):
    movies_all_info = []

    for movie in movies:
        tmp_one_ele = {}
        tmp_one_ele["id"] = movie.get("id")
        tmp_one_ele["title"] = movie.get("title")
        tmp_one_ele["poster_path"] = movie.get("poster_path")
        tmp_one_ele["vote_average"] = movie.get("vote_average")
        tmp_one_ele["overview"] = movie.get("overview")
    
        genre_ids = list(movie.get("genre_ids"))


        genre_names = []
        for genre_id in genre_ids:
            for one_ele_in_genres in genres:
                if one_ele_in_genres.get('id') == genre_id:
                    genre_names.append(one_ele_in_genres.get('name'))
        
        tmp_one_ele["genre_names"] = genre_names
        movies_all_info.append(tmp_one_ele)
    
    return movies_all_info
      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
