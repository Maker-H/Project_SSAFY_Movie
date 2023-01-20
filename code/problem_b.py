import json
from pprint import pprint


def movie_info(movie, genres):
    movie_shawshank = {}

    movie_shawshank["id"] = movie.get("id")
    movie_shawshank["title"] = movie.get("title")
    movie_shawshank["poster_path"] = movie.get("poster_path")
    movie_shawshank["vote_average"] = movie.get("vote_average")
    movie_shawshank["overview"] = movie.get("overview")
    genre_ids = list(movie.get("genre_ids"))


    genre_names = []

    for genre_id in genre_ids:
        for one_ele_in_dict in genres:
            if one_ele_in_dict.get('id') == genre_id:
                genre_names.append(one_ele_in_dict.get('name'))
    
    movie_shawshank["genre_names"] = genre_names
    
    return movie_shawshank
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
