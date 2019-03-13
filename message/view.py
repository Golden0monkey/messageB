#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.11
视图函数
'''


from flask import flash,render_template,redirect,url_for

from message import app
from message.forms import HelloForm


@app.route('/',methods=['GET','POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    return render_template('index.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)

