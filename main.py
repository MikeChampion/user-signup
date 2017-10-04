from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/add", methods=['GET', 'POST'])
def validate():
    #user_name = request.form['username']
    #password = request.form['password']
    #password2 = request.form['password2']
    #email = request.form['email']
    return render_template('welcome.html', username='user_name')

@app.route("/")
def index():
    return render_template('layout.html')

app.run()