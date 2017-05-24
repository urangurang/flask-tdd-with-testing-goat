from flask import render_template, request, redirect, url_for
from blog.base import base
from blog.base.models import Item, List
from blog.database import db_session


@base.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@base.route('/lists/<int:list_id>/', methods=['GET', 'POST'])
def view_list(list_id):
    items = Item.query.filter(Item.list == list_id).all()
    return render_template('list.html', items=items)


@base.route('/lists/new', methods=['GET', 'POST'])
def new_list():
    list_ = List()
    db_session.add(list_)
    db_session.commit()
    item = Item(text=request.form['item_text'], list=list_.id)
    db_session.add(item)
    db_session.commit()
    return redirect(url_for('base.view_list', list_id=list_.id))
