## Index
### 1. [✔️popular_count( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%EF%B8%8Fpopular_count-)
### 2. [✔️vote_average_movies( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%EF%B8%8Fvote_average_movies-)
### 3. [✔️ranking( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%EF%B8%8Franking-)
### 4. [✔️recommendation( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%EF%B8%8Frecommendation-)
### 5. [✔️credits( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%EF%B8%8Fcredits-)
### 6. [🚀프로젝트 회고!](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/02_pjt#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0---20230127)



---

<br>
<br>

# *problem_a*

## ✔️popular_count( )
> 현재 인기있는 영화의 개수를 반환하는 함수

### 필요 정보
- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
- 응답받은 데이터의 영화 개수를 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/214997396-416154d4-ec26-4cb4-8b33-07f8b68c39b8.png)

<br>
<br>

# *problem_b*

## ✔️vote_average_movies( )
> 8점 이상인 영화 목록을 반환하는 함수

### 필요 정보
- TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
- 응답받은 데이터 중 평점이 8점 이상인 영화 목록 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/214998185-a2910f4f-efdc-41b3-86ce-afab9a4b597e.png)


<br>
<br>

# *problem_c*

## ✔️ranking( )
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

## ✔️recommendation( )
> 제공된 영화 제목을 검색하여 추천 영화 목록을 반환하는 함수

### 필요 정보
- 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)
- 제공된 영화중 **첫번째 영화의** id를 기준으로 해당 영화에 대한 추천 영화 목록(Get Recommendations)을 가져옴  
- 추천 영화 목록 중 **첫번째 영화만** 반환

### 제약 사항
- 검색한 영화 정보가 없다면 None 반환
- 추천 영화 없을 경우 [] 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/215000855-7a9f23d3-fc87-43bd-a1fb-dd7b76d8fa2e.png)


<br>
<br>

# *problem_e*

## ✔️credits( )
> 제공된 영화 제목을 검색하여 해당 영화의 출연진(cast)과 스태프(crew) 중 연출진(Directing)의 이름을 반환하는 함수

### 필요 정보
- 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)
- 제공된 영화 중 **첫번째 영화의** id를 기준으로 해당 영화에 대한 출연진과 스태프 목록(Get Credits)를 가져옴  
- 데이터 추출하여 반환
  - 출연진 : cast_id 값이 10 미만이면 추출
  - 연출진 : 스태프 부서(department)가 Directing인 데이터만 추출

### 제약 사항
- 검색한 영화 정보가 없다면 None 반환

### 결과
![image](https://user-images.githubusercontent.com/83294376/215011719-3654a1c0-b43c-41f6-a272-6d462c3380c3.png)

<br>
<br>

# 프로젝트 회고 - 2023/01/27
`프로젝트 회고`

이번 프로젝트를 하면서 requests 라이브러리에 익숙해진거 같고 계속 데이터들을 다루다 보니 크롤링 자체에 익숙해진거 같습니다. 또한 API를 막연하게 생각했는데 이번 기회로 제가 어렵다고 생각한 것들이 어려운 것이 아닌 익숙하지 않은 것이라는 생각을 가지게 되었습니다. 실패할지라도 다음 배움의 초석이 될 수도 있으니 이 프로젝트를 계기로 새로운 것들에 많이 도전하고 싶습니다.  
