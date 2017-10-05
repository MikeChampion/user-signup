from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/login", methods=['GET', 'POST'])
def validation():
    username = request.form['user-name']
    #password = request.form['password']
    #password2 = request.form['password2']
    #email = request.form['email']
    
    error = None
    if len(username) < 3:
        error = "Username must be between 3 and 20 characters"
        return render_template("/layout.html")
    else:   
        pass     
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('layout.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()