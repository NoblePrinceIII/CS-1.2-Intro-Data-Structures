from flask import Flask, url_for, render_template
from histograms import *
from sample import *

app = Flask(__name__)

@app.route('/')
def index():
    text = 'word.txt'
    histograms = histogram(text)
    frequency = frequency(hist, 10)
    return render_template('index.html')



