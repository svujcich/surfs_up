# from flask import Flask

#add a new flask app instance
# **research "magic method", underscores before and after varible in function
# app = Flask(__name__)

# define starting point (root)
#forward slash says put data at the root of the route == highest level of hierarchy
# @app.route('/')
# def hello_world():
#     return 'Hello world'


#-------SET UP FLASK WEATHER APP----------

import datetime as dt
import json
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
from flask import jsonify 

#------SET UP DATABASE-----------------


# create function to access and query SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes (model)
Base = automap_base()
#reflect tables
Base.prepare(engine, reflect=True)

#save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

#--------SET UP FLASK------------------

#create a Flask application called "app"
app = Flask(__name__)

    # #ex. import app.py into another python file names example.py
    # import app
    # print("example __name__ = %s", __name__)
    # if __name__ == "__main__":
    #     print("example is being run directly.")
    # else:
    #     print("example is being imported")

#1a: define "welcome:"" route
@app.route("/")
#1b: create a function welcome() with a return statement
    # def welcome():
    #     return
#1c: add the precipitation, stations, tobs, and temp routes into return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')
#.\ == continue query to the next line

#2a: define "precipitation" route
@app.route("/api/v1.0/precipitation")
# def precipitation():
#     #2b: calculcate the date from 1 year ago to the most recent date in the 
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     #2c: write a query to get the date and precipitation for the previous year
#     precipitation = session.query(Measurement.date, Measurement.prcp).\
#         filter(Measurement.date >= prev_year).all()
#         #2d: Jsonify() -- create a dictionary with the date as the key and the precipitation as the value
#     precip = {date: prcp for date, prcp in precipitation}
#     return jsonify(precip)

def precipitation():

   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

if __name__=='__main__':
    app.run(debug=True)

#3a: define "stations" route
@app.route("/api/v1.0/stations")
#3b: create a new function called stations()
# def stations():
#     #3c: create a query to get all the stations in the database
#     results = session.query(Station.station).all()
#     #3d: convert the results to a list    
#     #3e. unravel results into one dimensional array w/ np.ravel( with results as the perameter)
#     #3f: to return our list as JSON,  add stations=stations, see flask documentation    
#     stations = list(np.ravel(results))
#     return jsonify(stations=stations)

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#4a: define temperature route
@app.route("/api/v1.0/tobs")
#4b: Create a function; def temp_monthly():.\ return 
# def temp_monthly():
#     #4c:calcualte date from "one year ago"
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     #4d: query the primary station for all the temperature observations from the previous year
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     #4e: unravel results into one dimensional array and convert to a list
#     temps = list(np.ravel(results))
#     #4f: jsonify temp list
#     return jsonify(temps=temps)

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#5a define route for min, max, and avg temps
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#5b create a function;def stats():.\ return
#5c: add start and end perameters; def stats(start=None, end=None):
#5d: create query, create a list called sel
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
#     #5d: add if-not statement to:
#     #   query database,
#     #   unravel the results,convert them to a list, 
#     #   jsonnify them to return them
#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)

#     #5e: get statistic data == calculate temp min average, and max with start and end dates
#     results = session.query(*sel).\
#         filter(Measurement.date >= start).\
#         filter(Measurement.date <= end).all()
#     temps = list(np.ravel(results))
#     return jsonify(temps)
    #5f: flask run in command line

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# to see min/ max/avg temps add date after address
#Example: /api/v1.0/temp/2017-06-01/2017-06-30