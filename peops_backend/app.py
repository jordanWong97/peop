from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/celebrities', methods=['GET', 'POST'])
def celebrities():
    if request.method == 'POST':
        return post_data()
    return {'celebrities': ['celeb1', 'celeb2', 'celeb3']}
