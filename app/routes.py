import re
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Post, User

# Testing -
# Development -
# Production -

# file-watcher


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        p = Post(email="lnreyes0688@gmail.com", image="", title="", body=request.form.get('body_text'))
        db.session.add(p)
        db.session.commit()
        flash('Success BLog Post Added!')
        return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/contact')
def contact():
    context = {
        'help': '',
        'page': 124567,
        'yellow': 'jaune'
    }
    return render_template('contact.html', **context)


@app.route('/blog')
def blog():
    # the whole point is for a user to post a blog and for me to post
    #create a route to elephant sequel to store the information
    #
    context = {
        'posts': [p.to_dict() for p in Post.query.all()]
    }
    return render_template('blog.html', **context)


#another route for user login and registration
@app.route('/login')
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        print(request.form)
        flash('Blog posted created successfully')
        return redirect(url_for('login'))
    return render_template('register.html')

#subscri button needs to also connect to the elephant sequel to store the info
