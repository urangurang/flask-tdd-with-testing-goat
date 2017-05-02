# FLASK TDD with TESTING GOAT

개발을 시작한지 2년 남짓 되었지만, 제대로 된 테스트 코드 하나 갖추지 못한채 개발을 하는 모습을 바꿔보고자 시작하게되었습니다.

[파이썬을 이용한 클린 코드를 위한 테스트 주도 개발](http://www.yes24.com/24/goods/16886031)의 Django 코드를 Flask로 구현했습니다. 그리고 테스팅에 사용된 unittest대신 pytest를 사용해보았습니다. 

기존 코드를 그대로 입력해볼 수도 있었지만, 기계적인 입력이 되는 것을 방지하고자 새롭게 코드를 짜며 책 내용을 반복하고 있습니다.

### 시작에 앞서

다음 링크에서 무료로 영문판 책 내용을 보실 수 있습니다.

[Test-Driven Development with Python](http://www.obeythetestinggoat.com/pages/book.html) 

본 예제는 파이썬 3.6.0 버전으로 실행됩니다.(3이상이면 큰 차이는 없을 것으로 예상됩니다.)

본 예제가 Flask와 Testing을 함께 공부하고자 하시는 분께 도움이 되었으면 합니다.

### 책과 달라진 점

- Django -> Flask 
- Django Template - > Jinja2
- Django ORM -> SQLAlchemy
- unnittest -> pytest

추가적으로 설치된 라이브러리 목록은 requirement.txt에 입력돼 있습니다. 


### 설치

실행에 앞서 파이썬3 가상환경에서 requirement.txt의 리스트 대로 설치해줍니다.

```
$ pip install -r requirement.text
```

본 예제에서 데이터베이스는 sqlite가 사용되었습니다. [다운로드](http://www.sqlite.org/download.html)

### 라이센스

본 예제는 MIT License 아래 보호되고 있습니다. 자세한 내용은 다음 파일을 참고해주세요. [LICENSE.md](LICENSE.md)

