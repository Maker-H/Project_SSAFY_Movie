Index
1. probelm_a
  - popular_count( )


---

<br>

# *problem_a*

## popular_count( )
> 현재 인기있는 영화의 개수를 반환하는 함수

### 필요 정보
- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
- 응답받은 데이터의 영화 개수를 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/214997396-416154d4-ec26-4cb4-8b33-07f8b68c39b8.png)

<br>
<br>

# *problem_b*

## vote_average_movies( )
> 8점 이상인 영화 목록을 반환하는 함수

### 필요 정보
- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
- 응답받은 데이터 중 평점이 8점 이상인 영화 목록 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/214998185-a2910f4f-efdc-41b3-86ce-afab9a4b597e.png)


<br>
<br>

# *problem_c*

## ranking( )
> 평점이 높은 5개의 영화 데이터 목록 반환하는 함수

### 필요 정보
- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
- 평점(vote_average)을 기준으로 평점이 높은 5개의 정보를 반환
- **sort이나 sorted 함수 사용**

### 결과
![image](https://user-images.githubusercontent.com/83294376/214999585-cb60f340-5b80-4cfa-8468-814b06f3d2e7.png)

<br>
<br>

# *problem_d*

## recommendation( )
> 제공된 영화 제목을 검색하여 추천 영화 목록을 반환하는 함수

### 필요 정보
- 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)
- 제공된 영화의 id를 기준으로 해당 영화에 대한 추천 영화 목록(Get Recommendations)을 가져옴  
- 추천 영화 목록 중 **첫번째 영화만** 반환

### 제약 사항
- 검색한 영화 정보가 없다면 None 반환
- 추천 영화 없을 경우 [] 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/215000855-7a9f23d3-fc87-43bd-a1fb-dd7b76d8fa2e.png)
