from blog import app
from flask import request, render_template, make_response
from blog.base.views import index


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
            assert res == expected_html

    def test_home_page_can_save_a_post_request(self):
        with app.test_client() as client:
            keyword = '신규 작업 아이템'
            rv = client.post('/', data=dict(item_text=keyword))
            assert keyword in rv.data.decode('utf-8')
            expected_html = render_template('index.html', new_item_text=keyword)
            assert index() == expected_html
