from flask import Flask, jsonify
import pandas as pd
import numpy as np
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
engine = create_engine("")
Base = automap_base()
Base.prepare(engine, reflect=True)

# import csv
# with open(".../Resources/winemag-data-130k-v2.csv") as f:
#     reader = csv.reader(f)
#     header = next(reader)


country = Base.classes.country
points = Base.classes.points
price = Base.classes.price
provinceState = Base.classes.province
varietyTYPE = Base.classes.variety

# Flask Setup
session = Session(engine)
app = Flask(__name__)

# Flask Routes
@app.route("")




