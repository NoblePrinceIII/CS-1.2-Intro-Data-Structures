from flask import Flask, render_template, request
import requests
import json
import os
app = Flask(__name__)

# route the function
@app.route('/')
def index():
    """Return homepage."""
    source_code = 'words.txt'
    return render_template("index.html")


    # get the top 10 GIFs for the search term
    # links to terminal
if __name__ == '__main__':
    app.run(debug=True)
