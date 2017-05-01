from flask import render_template, request
from blog.base import base


@base.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template('index.html', new_item_text=request.form.get('item_text', None))
    return render_template('index.html')
