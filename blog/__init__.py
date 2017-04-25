# __init__.py
# Flask main settings

from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')


from blog.posts.views import posts
from blog.base.views import base

app.register_blueprint(posts)
app.register_blueprint(base)