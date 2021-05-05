from flask import render_template
from myapp import app

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