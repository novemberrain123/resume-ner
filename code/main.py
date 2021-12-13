from flask import Flask, request, render_template
import os 
from misc import search

app = Flask(__name__)

#generate home page for user query
@app.route("/")
def index():    
    return render_template('index.html')

#generate result page
@app.route('/', methods=['POST'])
def my_form_post():
    if request.form['button'] == 'spacy':
        ner = 'spacy'
    if request.form['button'] == 'flair':
        ner = 'flair'

    text = request.form['text']
    #returns list containing file indexes
    matches, special = search(text, ner)
    return render_template('result.html', idxs = matches, len_idxs = len(matches), ner = ner, special = special)

