from flask import render_template

from blog.posts import posts


@posts.route('/posts')
def board_index():
    return render_template('posts.html')

