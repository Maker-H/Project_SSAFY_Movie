## Index
### [1. probelm_a - ✔️movie_info( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#movie_info-)
### [2. problem_b - ✔️movie_info( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#movie_info--1)
### [3. problem_c - ✔️movie_info( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#movie_info--2)
### [4. ✔️max_revenue( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#max_revenue-)
### [5. ✔️dec_movies( )](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#dec_movies-)
### [6. 🚀프로젝트 회고!](https://github.com/Maker-H/Project_SSAFY_Movie/tree/master/01_pjt#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0---20230120)

---
<br>
<br>


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

<br>
<br>

# *problem_e*  

## dec_movies( )
> 12월에 개봉한 영화들의 제목 리스트를 반환하는 함수

### 필요 정보
* `movies 폴더` 에서 각 파일의 **release_date** 확인
* 개봉일이 12월인 영화들의 제목을 리스트로 반환
    * *orginal_title*이 아닌 **title** 사용

### 결과
![image](https://user-images.githubusercontent.com/83294376/213616337-6b70edcc-3941-4b9f-955e-8a9e7472b048.png)


<br>
<br>

# 프로젝트 회고 - 2023/01/20
`배운점`

다른 파일들을 이용해서 정보를 뽑아내는 경험을 이번 관통 프로젝트에서 처음 해보았습니다. 기초 문법들을 배우다 보면 단편적인 느낌에 이게 정말 프로그램이 되고 웹에 구현이 된다고? 라는 생각이 드는데 이번 프로젝트를 통해 정말 내가 무언가를 유용한 지식을 배우고 있다는 것을 느꼈습니다. 구현부터 배포까지 스스로 할 수 있게 되는 미래가 기대됩니다^^
<br><br>

`프로젝트 회고`

이번 프로젝트에서는 커밋 로그에 신경을 써보았습니다. 커밋 제목을 doc과 feat으로 구별하여 한 함수를 구현할때마다 해당 함수에 해당되는 doc(README.md)과 feat(기능)을 차근차근 쌓아보았습니다.

요구사항을 한 번에 README에 정리한 후 feat을 쌓을지 doc과 feat을 차근차근 번갈아가면서 작성할지 고민하였지만 객체를 지향한다면 기능당 doc와 feat를 쌓는 것이 맞다고 판단했습니다. 또한 지금은 프로젝트 규모가 작아 README를 한 번에 작성할 수 있겠지만 추후에 요구사항의 규모가 커진다면 README를 계속 수정하게 될 수도 있지 않을까? 라는 생각도 커밋 로그를 하나씩 쌓게된 계기입니다. 

또한 하나의 폴더를 두 개의 레포지토리에 동시에 올려보는 시도를 하였습니다. SSAFY에서 사용하는 git lab과 개인적으로 사용하는 github에 동시에 올리고 싶다는 마음에서 시작된 도전입니다. 이 과정에서 branch가 protected로 설정된 문제가 있었지만 해결하여 git push 명령어를 통해 git lab과 github에 코드를 한 번에 push할 수 있게 되었습니다.

