import cgi
from flask import Flask, request, redirect, render_template


app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/validate", methods=['GET', 'POST'])
def validation():
    username = request.form['user-name']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    valid=True
    username_error=''
    password_error=''
    password2_error=''
    email_error=''

    if (len(username) >20) or (len(username) <3):
        username_error='Username must be between 3 and 20 characters'
        valid=False
    if len(password) >20 or len(password) <3:
        password_error='Password must be between 3 and 20 characters'
        valid=False
    if password2!=password or password2=='':
        password2_error='Password does not match'
        valid=False
    if email!="":
        if len(email) >20 or len(email) <3 or '@' not in email or '.' not in email:
            email_error='Email must be between 3 and 20 characters and contain . and @'
            valid=False
    if valid is False:    
        return render_template('layout.html', username_error=username_error, password_error=password_error, password2_error=password2_error, email_error=email_error)
    
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('layout.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()