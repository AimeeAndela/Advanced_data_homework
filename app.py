import numpy as np

import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return precipitation"""
    # Query precipitation
    results = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date > '2016-08-23').\
    order_by(measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(station.station).all()
    session.close()

    all_stations = list(np.ravel(results))

   # stations = []
    ##for stations in unique:
     #   stations_dict = {}
    #    stations_dict["station"] = station
     #   stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(measurement.date, measurement.tobs).\
    filter(measurement.date > '2016-08-23').\
    order_by(measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)


@app.route("/api/v1.0/start")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of minimum temperature, the average temperature, and the max temperature"""
    # Query minimum temperature, the average temperature, and the max temperature
    results = session.query(measurement.date, func.min(measurement.tobs)).all()
    filter(measurement.date > 2010-4-13, measurement.tobs)
    min(results)

    results_max = session.query(measurement.date, func.max(measurement.tobs)).all()
    filter(measurement.date > 2010-4-13, measurement.tobs)
    max(results_max)

    results_average = session.query(measurement.date, func.avg(measurement.tobs)).all()
    filter(measurement.date > 2010-4-13, measurement.tobs)
    max(results_average)
    
    session.close()

    # Convert list of tuples into normal list
    min_temp = list(np.ravel(results))
    max_temp = list(np.ravel(results_max))
    avg_temp = list(np.ravel(results_average))

    return jsonify(min_temp, max_temp, avg_temp)


@app.route("/api/v1.0/start/end")
def start_end():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    date = dt.datetime(2010, 4, 13)
    end_date = dt.datetime(2010, 8, 25)

    """Return a list of minimum temperature, the average temperature, and the max temperature"""
    # Query minimum temperature, the average temperature, and the max temperature
    results = session.query(measurement.date, func.min(measurement.tobs)).all()
    filter(measurement.date > date, measurement.tobs)
    min(results)

    results_max = session.query(measurement.date, func.max(measurement.tobs)).all()
    filter(measurement.date > date, measurement.tobs)
    max(results_max)

    results_average = session.query(measurement.date, func.avg(measurement.tobs)).all()
    filter(measurement.date > date, measurement.tobs)
    max(results_average)
    
    session.close()

    # Convert list of tuples into normal list
    min_temp = list(np.ravel(results))
    max_temp = list(np.ravel(results_max))
    avg_temp = list(np.ravel(results_average))

    return jsonify(min_temp, max_temp, avg_temp)


if __name__ == '__main__':
        app.run(debug=True)