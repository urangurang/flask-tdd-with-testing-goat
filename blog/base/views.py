from flask import render_template, make_response, url_for, Response

from blog.base import base


@base.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@base.route('/test', methods=['GET', 'POST'])
def test():
    res = make_response(render_template('index.html'))
    return res