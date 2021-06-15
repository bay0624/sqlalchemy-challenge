# Climate Analysis and Exploration
Using Python and SQLAlchemy to do basic climate analysis and data exploration of climate database in Hawaii. I used SQLAlchemy ORM queries, Pandas, Seaborn and Matplotlib to complete these analysis.

## Precipitation Analysis Steps
 - Two CSV files provided (hawaii_measurements.csv - which measures the daily precipitation and temperature from 2010 to 2017; and hawaii_stations.csv - which comprises of all the stations responsible for the measurements).
 - These two files were then used to create a sqLite database - hawaii.sqlite.
 - I then used SQLAlchemy create_engine to connect to the sqlite database.
 - SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.
 - Then finally linking Python to the database by creating a SQLAlchemy session.
