import json


def max_revenue(movies):
    revenue_with_movie = {}
    for one_ele_movie in movies:
        movie_id = one_ele_movie.get('id')
        movie_file_name = f'data/movies/{movie_id}.json'
        movie_json = open(movie_file_name, encoding='utf-8')
        movie_list = json.load(movie_json)

        revenue_with_movie[movie_list.get('revenue')] = movie_list.get('title')

    revenues_with_movies = sorted(revenue_with_movie.items(), reverse=True)
    
    top_revenue_movie_title = revenues_with_movies[0][1]

    return top_revenue_movie_title

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
