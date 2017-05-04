from blog import app
from flask import request, render_template
from blog.base.views import index, view_list
from blog.base.models import Item
from blog.database import db_session
from sqlalchemy import or_


class TestNewList(object):
    def test_saving_a_post_request(self):
        with app.test_client() as client:
            keyword = '포스트 저장용'
            client.post('/lists/new', data=dict(item_text=keyword))
            items = Item.query.filter(Item.text == '포스트 저장용').all()

            # 마지막에 추가된 레코드
            assert items[0].text == keyword
            Item.query.filter(Item.text == '포스트 저장용').delete()
            db_session.commit()
            assert Item.query.filter(Item.text == '포스트 저장용').count() == 0

    def test_redirects_after_post(self):
        with app.test_client() as client:
            rv = client.post('/lists/new', data=dict(item_text='신규 작업 아이템'))
            # print(rv) <Response streamed [302 FOUND]>
            # print(type(rv)) <class 'flask.wrappers.Response'>
            assert rv.status_code == 302
            assert '/lists/the-only-list-in-the-world/' in rv.location
            assert request.path == '/lists/new'
            Item.query.filter(Item.text == '신규 작업 아이템').delete()
            db_session.commit()
            assert Item.query.filter(Item.text == '신규 작업 아이템').count() == 0


class TestLiveView(object):
    def test_displays_all_items(self):
        item_01 = Item(text='itemey 1')
        item_02 = Item(text='itemey 2')
        db_session.add(item_01)
        db_session.add(item_02)
        db_session.commit()
        with app.test_request_context('/lists/the-only-list-in-the-world/'):
            res = view_list()
            assert item_01.text in res
            assert item_02.text in res
        # or_ 사용해서 위에 입력한 테스트 값을 지워줍니다.
        db_session.query(Item).filter(or_(Item.text == 'itemey 1',
                                          Item.text == 'itemey 2')).delete()
        db_session.commit()

    def test_uses_list_template(self):
        with app.test_request_context('/lists/the-only-list-in-the-world/'):
            # self.assertTemplateUsed - Django test function
            # res = view_list()
            # assert res != render_template('list.html')
            pass


class TestItemModel(object):

    def test_saving_and_retrieving_items(self):
        first_item = Item(text='첫 번째 아이템')
        second_item = Item(text='두 번째 아이템')
        db_session.add(first_item)
        db_session.add(second_item)
        db_session.commit()

        saved_items = Item.query.filter(or_(Item.text == '첫 번째 아이템', Item.text == '두 번째 아이템')).all()

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        assert first_saved_item.text == '첫 번째 아이템'
        assert second_saved_item.text == '두 번째 아이템'
        Item.query.filter(Item.text == '첫 번째 아이템').delete()
        Item.query.filter(Item.text == '두 번째 아이템').delete()
        db_session.commit()


class TestMainPageSetUp(object):

    def test_root_url_resolves_to_welcome_page_view(self):
        with app.test_request_context('/', method='GET'):
            module = index.__module__.split('.')[1]  # index의 모듈 blog.base.views
            func = index.__name__  # index
            assert request.endpoint in module + '.' + func

    def test_welcome_page_returns_correct_html(self):

        with app.test_request_context('/', method='GET'):
            res = index()  # type 'str', rendered html
            expected_html = render_template('index.html')  # type 'str', rendered html

            assert res.startswith('<!DOCTYPE html>')
            assert '<title>To-Do lists</title>' in res
            assert res.endswith('</html>')
            # table에 데이터베이스의 값이 들어오면서 index()의 반환값과 index.html의 값이 달라지게 됩니다.
            assert res == expected_html