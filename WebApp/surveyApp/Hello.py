from flask import Flask
app = Flask(__name__)

@app.route('/')
def first_func():
   return "<h1>Work in progress. Will be updated soon.</h1>"

if __name__ == '__main__':
   app.run()