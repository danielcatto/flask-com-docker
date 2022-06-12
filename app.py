# compose_flask/app.py
from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


@app.route('/<user_id>')
def index(user_id="visistante"):
   id = user_id
   return render_template('index.html', id = id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)