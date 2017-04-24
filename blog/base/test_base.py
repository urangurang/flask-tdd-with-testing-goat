from blog import app
from flask import request
from blog.base.views import index


class TestMainPageSetUp(object):

    def test_root_url_resolves_to_welcome_page_view(self):
        with app.test_request_context('/', method='GET'):
            module = index.__module__.split('.')[1]  # index의 모듈 blog.base.views
            func = index.__name__  # index
            assert request.endpoint in module + '.' + func

    def test_welcome_page_returns_correct_html(self):
        with app.test_request_context('/', method='GET'):
            res = index()  # res type - class 'str'
            assert res.startswith('<!DOCTYPE html>')
            assert '<title>To-Do lists</title>' in res
            assert res.endswith('</html>')
