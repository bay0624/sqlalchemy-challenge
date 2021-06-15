# Climate Analysis and Exploration
Using Python and SQLAlchemy to do basic climate analysis and data exploration of climate database in Hawaii. I used SQLAlchemy ORM queries, Pandas, Seaborn and Matplotlib to complete these analysis.

## Precipitation Analysis Step 1
 - Two CSV files provided (hawaii_measurements.csv - which measures the daily precipitation and temperature from 2010 to 2017; and hawaii_stations.csv - which comprises of all the stations responsible for the measurements).
 - These two files were then used to create a sqLite database - hawaii.sqlite.
 - I then used SQLAlchemy create_engine to connect to the sqlite database.
 - SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.
 - Then finally linking Python to the database by creating a SQLAlchemy session.

## Precipitation Analysis Step 2
- After establishing link, I then used SQLAlchemy ORM queries to find the most recent date in the data set.
- Using this date, I retrieved the average precipitation per day for the previous 12 months, in ascending order.
- The query results were then loaded into a Pandas DataFrame and the index was set to the date column.
- I then proceeded to plot the results using the Seaborn.

![image](https://user-images.githubusercontent.com/53978733/121991017-cd551780-cd6c-11eb-875d-e66a3a99ea91.png)

## Station Analysis
- Designed a query to calculate the total number of stations in the dataset.
- Designed a query that lists all stations with their corresponding observation count in descending order to determine which station is the most active (i.e., has the greatest number of observations).
- Calculated the lowest, highest, and average temperature for that station id (i.e., the one with the greatest number of observations).
- Designed a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.
- Then plotted the results as a histogram with bins=12.

![image](https://user-images.githubusercontent.com/53978733/121991227-40f72480-cd6d-11eb-8958-04ac672e2ded.png)


