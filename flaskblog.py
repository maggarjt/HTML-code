from flask import Flask, render_template, url_for
from forms import RegistrationForms, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'be0116671b56cc6731430146985707fa'
# key created by import secrets secrets.token_hex(16) for 16 bit code using python interpreter and copy/pasted
posts = [
	{
		'author': 'Jesse Maggard',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 16, 2020'
	},
	{
		'author': 'Ian Abbott',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 17, 2020'
	}
]
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html, title='Register, form=form)






if __name__ == '__main__':
	app.run(debug=True)