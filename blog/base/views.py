from flask import render_template, request, redirect
from blog.base import base
from blog.base.models import Item
from blog.database import db_session


@base.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        new_item_text = request.form['item_text']
        item = Item(text=new_item_text)
        db_session.add(item)
        db_session.commit()
        return redirect('/')
    items = Item.query.all()
    return render_template('index.html', items=items)
