from flask import Flask, render_template
import pandas as pd
import numpy as np
from pymongo import MongoClient
from bson.json_util import dumps

# Create an instance of MongoClient
mongo = MongoClient(port=27017)

# assign the met database to a variable name
db = mongo['project_3']

# assign the collection to a variable
wine_table = db['wine_table']

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

# load the template / html
@app.route("/pie")
def pie():
    return render_template('pie.html')

# loads chart data
@app.route("/piedata")
def piedata():
    query = {"points": 87}
    data = wine_table.find_one(query)
    # add filtering logic here, and set filteredData to it
    filteredData = data
    return dumps(filteredData)

# load the template / html
@app.route("/bubble")
def bubble():
    return render_template('bubble.html')

# loads chart data
@app.route("/bubbledata")
def bubbledata():
    query = {"points": 87}
    data = wine_table.find_one(query)
    # add filtering logic here, and set filteredData to it
    filteredData = data
    return dumps(filteredData)

# load the template / html
@app.route("/bar")
def bar():
    return render_template('bar.html')

# loads chart data
@app.route("/bardata")
def bardata():
    query = {"points": 87}
    data = wine_table.find_one(query)
    # add filtering logic here, and set filteredData to it
    filteredData = data
    return dumps(filteredData)

# load the template / html
@app.route("/scatter")
def scatter():
    return render_template('scatter.html')

# loads chart data
@app.route("/scatterdata")
def scatterdata():
    query = {"points": 87}
    data = wine_table.find_one(query)
    # add filtering logic here, and set filteredData to it
    filteredData = data
    return dumps(filteredData)

if __name__ == "__main__":
    app.run(debug=True)
