from flask import Flask, request, render_template
from search import search
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #returns list containing file indexes
    idxs = search(text)
    return render_template('result.html', idxs)