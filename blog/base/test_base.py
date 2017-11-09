from blog import app
from flask import request, render_template
from blog.base.views import index, view_list
from blog.base.models import Item, List
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
            assert '/lists/' in rv.location
            assert request.path == '/lists/new'
            Item.query.filter(Item.text == '신규 작업 아이템').delete()
            db_session.commit()
            assert Item.query.filter(Item.text == '신규 작업 아이템').count() == 0


class TestLiveView(object):
    def test_displays_only_items_for_that_list(self):
        correct_list = List()
        db_session.add(correct_list)
        db_session.commit()
        item_01 = Item(text='itemey 1', list=correct_list.id)
        item_02 = Item(text='itemey 2', list=correct_list.id)
        db_session.add(item_01)
        db_session.add(item_02)
        db_session.commit()

        other_list = List()
        db_session.add(other_list)
        db_session.commit()
        other_item_01 = Item(text='다른 목록 아이템 1', list=other_list.id)
        other_item_02 = Item(text='다른 목록 아이템 2', list=other_list.id)

        with app.test_request_context('/lists/%d' % correct_list.id):
            res = view_list(list_id=correct_list.id)
            assert item_01.text in res
            assert item_02.text in res
            assert other_item_01.text not in res
            assert other_item_02.text not in res
            Item.query.filter(Item.list == correct_list.id).delete()
            Item.query.filter(Item.list == other_list.id).delete()
            db_session.commit()
            List.query.filter(List.id == correct_list.id).delete()
            List.query.filter(List.id == other_list.id).delete()
            db_session.commit()

    def test_uses_list_template(self):
        with app.test_client() as client:
            list_ = List()
            db_session.add(list_)
            db_session.commit()
            client.get('/lists/%d/' % list_.id)


class TestListAndItemModels(object):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        db_session.add(list_)
        db_session.commit()

        first_item = Item(text='첫 번째 아이템', list=list_.id)
        second_item = Item(text='두 번째 아이템', list=list_.id)
        db_session.add(first_item)
        db_session.add(second_item)
        db_session.commit()

        saved_items = Item.query.filter(or_(Item.text == '첫 번째 아이템', Item.text == '두 번째 아이템')).all()

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        assert first_saved_item.text == '첫 번째 아이템'
        assert first_saved_item.list == list_.id
        assert second_saved_item.text == '두 번째 아이템'
        assert second_saved_item.list == list_.id

        Item.query.filter(Item.text == '첫 번째 아이템').delete()
        Item.query.filter(Item.text == '두 번째 아이템').delete()
        List.query.filter(List.id == list_.id).delete()
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
            expected_html = render_template('home.html')  # type 'str', rendered html

            assert res.startswith('<!DOCTYPE html>')
            assert '<title>To-Do lists</title>' in res
            assert res.endswith('</html>')
            # table에 데이터베이스의 값이 들어오면서 index()의 반환값과 index.html의 값이 달라지게 됩니다.
            assert res == expected_html


class TestNewItem(object):

    def test_can_save_a_post_request_to_an_existing_list(self):
        other_list = List()
        correct_list = List()

        db_session.add(other_list)
        db_session.add(correct_list)
        db_session.commit()

        with app.test_client() as client:
            client.post(
                '/lists/%d/add_item' % (correct_list.id,),
                data=dict(item_text='기존 목록에 신규 아이템')
            )