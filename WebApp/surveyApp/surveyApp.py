from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def loginForm():
   return render_template('loginForm.html')

if __name__ == '__main__':
   app.run(debug=True)
