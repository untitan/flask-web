from flask import Flask, url_for, redirect, render_template

import config

app = Flask(__name__)
app.config.from_object(config)


class UserInfo(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


@app.route('/')
def index():
    userinfo = UserInfo('花卷大王', 18, 88)
    return render_template('index.html', userinfo=userinfo)


@app.route('/list')
def list():
    userlist = []
    for u in range(10):
        userlist.append(UserInfo('花卷大王', u + 1, 80 + u))
    return render_template('list.html', userlist=userlist)


@app.route('/login')
def login():
    return 'login'


@app.route('/blog/<is_login>')
def blog(is_login):
    if is_login == '1':
        return 'blog'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
