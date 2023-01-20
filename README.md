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
> 제공되는 영화 데이터의 중요내용을 수정해 반환하는 함수

### 필요 정보
* `movie.json`에서 필요한 정보에 해당 하는 값 추출
    * id, title, poster_path, vote_average, overview, genre_ids
* `movie.json` 에서 추출한 *genre_ids를* `genre.json` 을 이용하여 각 장르 번호에 맞는 name 값으로 *대체한 genre_names* 생성
* 필요한 정보를 포함하는 새로운 딕셔너리로 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/213604791-9d83f41d-f8d5-4c9a-9fbf-70d766898391.png)


<br>

# *problem_c*  

## movie_info( )
> 필요한 정보만 추출해 반환하는 함수

### 필요 정보
* `movies.json`에서 필요한 정보에 해당 하는 값 추출
    * id, title, poster_path, vote_average, overview, genre_ids
* `movies.json` 에서 추출한 *genre_ids를* `genre.json` 을 이용하여 각 장르 번호에 맞는 name 값으로 *대체한 genre_names* 생성 
* id, title, poster_path, vote_average, overview, **genre_names**가 포함된 새로운 리스트 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/213607576-3fe9672a-0f1b-482d-8e43-153a08f12ec6.png)

<br>

# *problem_d*  

## max_revenue( )
> 영화 중 가장 높은 수익을 낸 영화를 반환하는 함수

### 필요 정보
* `movies 폴더` 에서 각 파일의 revenue 확인
* revenue가 가장 높은 영화의 제목을 반환
    * *orginal_title*이 아닌 **title** 사용

### 결과
![image](https://user-images.githubusercontent.com/83294376/213614674-71d0038f-3305-4c75-99f1-d0921cb8a1d6.png)



