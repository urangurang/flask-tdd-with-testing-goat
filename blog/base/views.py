from flask import render_template
from blog.base import base


@base.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')