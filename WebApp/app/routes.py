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
    if request.method == 'POST':
        loginForm.email.data=request.form['email']
        loginForm.password.data=request.form['password']      
        user = User.query.filter_by(email=loginForm.email.data).first()
        if user is None:
            flash('Invalid email', category='danger')
            return redirect(url_for('login'))
        if not user.check_password(loginForm.password.data):
            flash("Wrong Password", category="danger")
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('survey')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=loginForm)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('survey'))
    signupform = SignUpForm()
    if request.method == 'POST':
        signupform.username.data=request.form['username']
        signupform.email.data=request.form['email']
        signupform.password.data=request.form['password']
        user = User.query.filter_by(username=signupform.username.data).first()
        if user is not None:
            flash("Please use a different username")
            return redirect(url_for('signup'))
        user = User.query.filter_by(email=signupform.email.data).first()
        if user is not None:
            flash("Please use a different email address")
            return redirect(url_for('signup'))
        user = User(username=signupform.username.data, email=signupform.email.data)
        user.set_password(signupform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', category='success')
        return redirect(url_for('login'))
    #else: 
       # flash("Sign Up Failed")
    return render_template('signup.html', form=signupform)


@app.route('/results',methods=['GET','POST'])
@login_required
def results():
    if request.method == 'POST':
        if current_user.is_authenticated:
            current_user.surveyTaken = 1
            db.session.commit()
        choices=[1,2,3,4,5]
        choiceString = "a"
        with open("/home/adharsh/Desktop/webapp/app/adminSurvey.json", "r") as jsonFile:
            AddingVotesData = json.load(jsonFile)
            for i in range(0,len(AddingVotesData)):
                choiceString = request.form[str(i)]
                choices[i] = int(choiceString)
                AddingVotesData[i]["Choices"][choices[i]-1]["Votes"] = AddingVotesData[i]["Choices"][choices[i]-1]["Votes"] + 1
        with open("/home/adharsh/Desktop/webapp/app/adminSurvey.json", "w") as jsonFile:
            json.dump(AddingVotesData, jsonFile)
        flash('successsssss', category="success")
    Data=json.loads(open('/home/adharsh/Desktop/webapp/app/adminSurvey.json').read())
    votesData = []
    for i in range(0,len(Data)):
        votesData = votesData + [[ { "Votes":0 } for k in range(0, len(Data[i]["Choices"])) ]]
    for i in range(0,len(Data)):
        for j in range(0,len(Data[i]["Choices"])):
            votesData[i][j]["Votes"] = Data[i]["Choices"][j]["Votes"]
    return render_template('results.html', Data=Data, votesData=votesData)


@app.route('/survey',methods=['GET','POST'])
@login_required
def survey():
    if current_user.surveyTaken:
       flash('You have already taken the survey!')
       return redirect(url_for('results'))
    #flash("Logged in Successfully!", category='success')
    Data=json.loads(open('/home/adharsh/Desktop/webapp/app/adminSurvey.json').read())
    return render_template('survey.html', Data=Data)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))
