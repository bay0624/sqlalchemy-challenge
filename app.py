import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

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
    results = engine.execute("SELECT date, AVG(prcp) FROM measurement \
        WHERE date >= '2016-08-23' \
            GROUP BY date \
                ORDER BY date ASC").fetchall()
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
    results = engine.execute("SELECT station, COUNT(*) AS 'num_of_reports'\
                                 FROM measurement GROUP BY station\
                                 ORDER BY num_of_reports DESC").fetchall()
    session.close()

    stat_data = []
    for station, num_of_reports in results:
        stat_dict = {}
        stat_dict["station"] = station
        stat_dict["num_of_reports"] = num_of_reports
        stat_data.append(stat_dict)

    return jsonify(stat_data)


@app.route("/api/v1.0/tobs")
def tobs_data():
    session = Session(engine)
    results = engine.execute("SELECT date, tobs FROM measurement \
                      WHERE station = 'USC00519281' \
                      AND date >= '2016-08-23'").fetchall()
    session.close()

    temp_data = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temp"] = tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)


if __name__ == "__main__":
    app.run(debug=True)