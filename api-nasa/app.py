import os
from flask import Flask, jsonify, render_template
app = Flask(__name__)

#we define the route /
@app.route('/welcome')
def welcome():
    # return a json
    return jsonify({'status': 'api working'})

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))