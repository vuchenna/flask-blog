from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Posts
from application.forms import PostForm




@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all() 
    return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))

    return render_template('login.html', title = 'Login')



@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/post', methods=['GET','POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                title=form.title.data,
                content = form.content.data
             
            )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_templates('post.html',title='Post',form=form)





