from flask import Flask, url_for, render_template
from sample import *
from histograms import *

app = Flask(__name__)

@app.route('/')
def index():
    words = book('words.txt')
    number_of_words = 10
    histograms = histogram(words)
    frequency = frequency(histogram, number_of_words)

    return render_template('index.html', index=)

