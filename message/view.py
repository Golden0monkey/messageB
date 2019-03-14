#coding:utf-8
#!usr/bin/env python3.6
'''
author:shadow
date:2019.3.11
视图函数
'''


from flask import flash,render_template,redirect,url_for

from message import app,db
from message.forms import HelloForm
from message.models import Message,initdb


@app.route('/',methods=['GET','POST'])
def index():
    initdb();
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    return render_template('index.html', form=form, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)

