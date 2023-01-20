# *problem_a* 
## movie_info( )
> 영화 '쇼생크 탈출'의 정보를 담고 있는 함수

### 필요 정보
* `movie.json`에서 필요한 정보에 해당 하는 값 추출
    * id, title, poster_path, vote_average, overview, genre_ids
* 필요한 정보를 새로운 딕셔너리로 반환
### 결과
![image](https://user-images.githubusercontent.com/83294376/213602885-5976c6c4-7556-4dbf-bcb4-7204e13215b5.png)

<br>

# *problem_b*  

## movie_info( )
> 제공되는 영화 데이터의 중요내용을 수정하는 함수

### 필요 정보
* `movie.json`에서 필요한 정보에 해당 하는 값 추출
    * id, title, poster_path, vote_average, overview, genre_ids
* `movie.json` 에서 추출한 *genre_ids를* `genre.json` 을 이용하여 각 장르 번호에 맞는 name 값으로 *대체한 genre_names* 생성
* 필요한 정보를 포함하는 새로운 딕셔너리로 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/213604791-9d83f41d-f8d5-4c9a-9fbf-70d766898391.png)

