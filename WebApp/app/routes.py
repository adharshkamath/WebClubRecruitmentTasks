from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm, SignUpForm
from app.models import User
import json


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(email=loginForm.email.data).first()
        if user is None or not user.check_password(loginForm.password.data):
            flash('Invalid username or password')
            return render_template('login.html', title='Sign In', form=loginForm)
        login_user(user, remember=loginForm.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('survey')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=loginForm)


@app.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    signupform = SignUpForm()
    if signupform.validate_on_submit():
        user = User(username=signupform.username.data, email=signupform.email.data)
        user.set_password(signupform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=signupform)


@app.route('/results',methods=['GET','POST'])
#@login_required
def results():
    
    Data=json.loads(open('/home/adharsh/Desktop/WebSurvey/app/adminSurvey.json').read())
    votesData = []
    for i in range(0,len(Data)):
        votesData = votesData + [[ { "Votes":0 } for k in range(0, len(Data[i]["Choices"])) ]]
    for i in range(0,len(Data)):
        for j in range(0,len(Data[i]["Choices"])):
            votesData[i][j]["Votes"] = Data[i]["Choices"][j]["Votes"]
    return render_template('results.html', Data=Data, votesData=votesData)


@app.route('/survey',methods=['GET','POST'])
#@login_required
def survey():
#    if current_user.is_elegible:
#       flash('You have already taken the survey!')
#       return redirect(url_for('results'))
    
    Data=json.loads(open('/home/adharsh/Desktop/WebSurvey/app/adminSurvey.json').read())
    return render_template('survey.html', Data=Data)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))
