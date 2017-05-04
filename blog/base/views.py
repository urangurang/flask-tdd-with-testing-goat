from flask import render_template, request, redirect
from blog.base import base
from blog.base.models import Item
from blog.database import db_session


@base.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@base.route('/lists/the-only-list-in-the-world/', methods=['GET', 'POST'])
def view_list():
    items = Item.query.all()
    return render_template('list.html', items=items)


@base.route('/lists/new', methods=['GET', 'POST'])
def new_list():
    item = Item(text=request.form['item_text'])
    db_session.add(item)
    db_session.commit()
    return redirect('/lists/the-only-list-in-the-world/')
