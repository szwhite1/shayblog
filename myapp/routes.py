from flask import render_template, flash, redirect, url_for
from myapp import app
from myapp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Shay'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Laurel!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie is the best movie ever!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
		flash('The website is coming along nicely!')
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)