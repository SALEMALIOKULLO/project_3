from flask import Flask, render_template
import pandas as pd
import numpy as np
from pymongo import MongoClient
from pprint import pprint
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
    # match query to find only "country" where "US" is the value
    match_query = {'$match':{"country": {'$regex': "US"}}}
    # aggregation query that counts the number of documents grouped by "country", then "province"
    group_query = {'$group': {'_id': {"country": "$country",
                                      "province": "$province"}, 
                                'count': {'$sum': 1}
                            }
                    }
    #creates a dictionary to allow the pipeline to sort by "province" in alphabetical order
    sort_values = {'$sort': {'province': 1}}
    #puts pipeline together
    pipeline = [match_query, group_query,sort_values]
    #runs pipeline through aggregate method & saves results to variable
    results = list(wine_table.aggregate(pipeline))

    #Count the rows in results (I believe it should be the equivalent of the amount of states that were logged)
    print("Number of rows in results", len(results))
    #pretty print the first 5 results
    pprint(results[0:5])

    # add filtering logic here, and set filteredData to it
    #will need to change
    filteredData = results
    return dumps(filteredData)

# load the template / html
@app.route("/box")
def bubble():
    return render_template('box.html')

# loads chart data
@app.route("/boxdata")
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
