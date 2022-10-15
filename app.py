# add dependencies
from flask import Flask,jsonify
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
from datetime import datetime

app = Flask(__name__)

def currentday():
    today = datetime.now()
    return today.strftime('%m-%d')

#set up database
engine = create_engine("sqlite:////Users/daniellesears/sqlalchemy-challenge.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station


#routes
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)"
    )

    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()
    prcp_data = list(np.ravel(results))
    return jsonify(prcp_data)

   #Return JSON list of stations from dataset
    @app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.name).all()
    station_list = list(np.ravel(results))
    return jsonify(station_list)

if __name__ == "__main__":
    app.run(debug=True)