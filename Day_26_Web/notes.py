from flask import Flask
import os

# Creating routes
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # for deployment we use the environ to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)