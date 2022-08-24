# 📚 wanted_pre_onboarding
 > <h2>📖 프리온보딩 백엔드 코스 4차 선발과제<h2>
 > 💡 사용 기술
 　　<img src="https://img.shields.io/badge/django-092E20?style=flat&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/>
 <img src="https://img.shields.io/badge/html5-E34F26?style=flat&logo=html5&logoColor=white"/>
 <img src="https://img.shields.io/badge/css3-1572B6?style=flat&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/sqlite-003B57?style=flat&logo=sqlite&logoColor=white"/>
 ><h2>💡 트리 구조<h2>
  ```
  📦 
  wanted
   ├─ .gitignore
   ├─ Scripts
   ├─ Unt
   ├─ config
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   ├─ manage.py
   ├─ pyvenv.cfg
   ├─ recruit
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ forms.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ static
   │  ├─ bootstrap.min.css
   │  └─ style.css
   └─ templates
      ├─ base.html
      └─ recruit
         ├─ notification_detail.html
         ├─ notification_form.html
         └─ notification_list.html
```
<h2>💡EER Diagram<h2>
<img src ="https://user-images.githubusercontent.com/99165573/185777690-d9727baa-b3e4-405c-a283-8db57ee3992c.png" width="600"> 

<h2>💡구현 목록<h2>  
1.채용공고 등록 <br>
2.채용공고 수정 <br>
3.채용공고 삭제 <br>
4.채용공고 목록 <br>
5.채용공고 검색 <br>
6.채용공고 상세 페이지 <br>
7.채용공고 지원

<h2>💡구현 상세 설명<h2>  
1. 채용공고를 등록합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185778730-b49ada5f-7d5c-4b2b-9e40-db88c7ab3b19.gif"> 
<img src ="https://user-images.githubusercontent.com/99165573/185779801-1fd2ec7d-4d9c-46a2-a5e0-eb1ebe9637ac.png"> 
 <h3> 요구조건에 맞게 채용공고 각 항목별로 입력합니다.(회사id는 미리 만들어놨다는 가정이 있습니다.)<h3>
 <h3> notification 테이블에 채용공고가 저장됩니다.<h3><br><br>
2. 채용공고를 수정합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185778885-d5ab7605-679a-4a1c-a0b4-d3b77ac7a816.gif">
<img src ="https://user-images.githubusercontent.com/99165573/185779801-1fd2ec7d-4d9c-46a2-a5e0-eb1ebe9637ac.png"> 
<img src ="https://user-images.githubusercontent.com/99165573/185780089-ebc7d154-d00f-4dac-a472-9893bb0ec790.png"> 
  <h3> 수정버튼 클릭 후, 채용공고의 상세정보를 수정합니다.<h3>
  <h3> notification 테이블의 데이터가 수정됩니다.<h3><br><br>
3. 채용공고를 삭제합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185779192-17c864a2-ffa8-463f-82a1-3142930fc66f.gif">
<img src ="https://user-images.githubusercontent.com/99165573/185780116-71646643-c8b0-4c30-b597-e3b53da2b956.png">
  <h3> 삭제버튼 클릭 후, 채용공고를 삭제합니다.<h3><br><br>
  <h3> notification 테이블의 데이터가 삭제됩니다.<h3>
4. 채용공고 목록을 조회합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185779339-8d066353-94e4-4f50-b0ab-ea577a42b733.png">
<img src ="https://user-images.githubusercontent.com/99165573/185780980-2743f880-dd16-49b7-94c9-a6310d3c5cc2.png">
 <h3> /recruit/링크에서 채용공고 목록을 조회할 수 있습니다.<h3>
 <h3> notification 테이블에 채용공고 데이터들을 볼 수 있습니다.<h3><br><br>
5. 채용공고 검색합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185779412-8f07c64a-a015-47f6-9b20-7e60ad3198a5.gif">
  <h3> 회사명,포지션 등 검색어를 입력해 관련 채용공고를 조회할 수 있습니다.<h3><br><br>
6. 채용공고 상세페이지에 접속합니다. <br>
<img src ="https://user-images.githubusercontent.com/99165573/185779484-5b887135-60f8-4c2a-aab1-d4c9e069407c.gif">
<img src ="https://user-images.githubusercontent.com/99165573/185780344-a28e8185-2745-4fbf-84aa-1252ba152540.png">
  <h3> 회사명,국가,지역,자격요건 등 채용공고에 관한 상세내용을 볼 수 있습니다.<h3>
7. 채용공고에 지원합니다.<br>
<img src ="https://user-images.githubusercontent.com/99165573/185779588-b7e1da26-cd42-42ac-8b82-65d741246907.gif">
<img src ="https://user-images.githubusercontent.com/99165573/185780849-7116613a-3c6c-4f0e-8217-a0edd1ef87fd.png">
<img src ="https://user-images.githubusercontent.com/99165573/185780898-b58f1168-65ce-47e5-90ab-cf1b743af37a.png">
<h3> 지원자가 id를 생성했다는 가정하에, 지원자id를 입력하면 지원완료가 됩니다.<h3>
<h3> user테이블을 보면 채용공고 id에 지원자 id 데이터가 함께 있다는 것을 알 수 있습니다.<h3><br><br>
