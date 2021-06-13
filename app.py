import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation_data():
    session = Session(engine)
    results = session.query(Measurement.date, func.avg(Measurement.prcp)).\
        filter(Measurement.date >= "2016-08-23").\
            group_by(Measurement.date).\
                order_by(Measurement.date)
    session.close()

    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_data.append(prcp_dict)
    
    return jsonify(prcp_data)


@app.route("/api/v1.0/stations")
def stations_data():
    session = Session(engine)
    results = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc())
    session.close()

    stat_data = []
    for station, num_of_reports in results:
        stat_dict = {}
        stat_dict["station_id"] = station
        stat_dict["reports"] = num_of_reports
        stat_data.append(stat_dict)

    return jsonify(stat_data)


@app.route("/api/v1.0/tobs")
def tobs_data():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
            filter(Measurement.date >= "2016-08-23")
    session.close()

    temp_data = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temp"] = tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)


@app.route("/api/v1.0/<start>")
def start_data(start):

    session = Session(engine)
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        group_by(Measurement.date).\
            filter(Measurement.date >= start).all()
    session.close()
    
    st_data = []
    for date, min, max, avg in results:
        st_dict = {}
        st_dict["date"] = date
        st_dict["min temp"] = min
        st_dict["max temp"] = max
        st_dict["average temp"] = avg
        st_data.append(st_dict)

    return jsonify(st_data)


@app.route("/api/v1.0/<start>/<end>")
def start_end_data(start, end):

    session = Session(engine)
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        group_by(Measurement.date).\
            filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    session.close()
    
    st_data = []
    for date, min, max, avg in results:
        st_dict = {}
        st_dict["date"] = date
        st_dict["min temp"] = min
        st_dict["max temp"] = max
        st_dict["average temp"] = avg
        st_data.append(st_dict)

    return jsonify(st_data)

if __name__ == "__main__":
    app.run(debug=True)