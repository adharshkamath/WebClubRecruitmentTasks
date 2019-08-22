from flask import Flask, render_template
import json #For parsing later

app = Flask(__name__)

@app.route('/')
def loginForm():
   return render_template('loginForm.html')

@app.route('/survey')
def survey():
       return render_template('surveyFile.html')

if __name__ == '__main__':
   app.run(debug=True)
