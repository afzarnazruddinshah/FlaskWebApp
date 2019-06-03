from flask import Flask, render_template, flash, redirect, url_for
from forms import SignupForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8acacb6a8e2e603569b481093becef9f'

posts = [ 

    {
        'title': 'My Blog 1',
        'author': 'Livingstone',
        'date': 'May 29, 2019'
    },
    {
        'title': 'My Blog 2',
        'author': 'Livingstone',
        'date': 'May 20, 2019'
    }
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index(name='New User', title='Index'):
    return render_template('index.html', name='Livingstone')

@app.route('/blog')
def blogs(title='Blog'):
    return render_template('fruits.html', posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup(title='SignUp'):
    form = SignupForm()
    if form.validate_on_submit() == True:
        flash(f'Account created for {form.username.data}')
        return redirect(url_for('index'))
    else:
        return render_template('signup.html',form=form, title='Intial')



    

app.run(debug=True)
