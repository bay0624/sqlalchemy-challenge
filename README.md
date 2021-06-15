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

## Climate App
Now that the initial analysis was completed. A Flask API app was designed (app.py), based on the queries developed above. Six routes were created and they are as follows:
Routes
- <b>/Home page</b>: List all routes that are available.
- <b>/api/v1.0/precipitation</b>: Lists most recent 12 months of precipitation data, converting the query results to a dictionary using date as the key and prcp as the value.
- <b>/api/v1.0/stations</b>: Returns a JSON list of stations from the dataset.
- <b>/api/v1.0/tobs</b>: Lists the dates and temperature observations of the most active station for the most recent 12 months of data. Returns a JSON list of temperature observations (TOBS) for that year.
- <b>/api/v1.0/{start}</b> and <b>/api/v1.0/{start}/{end}</b>: A query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date. When given the start and the end date, calculate the minimum, average, and maximum obvserved temperature for dates between the start and end date inclusive. Return a JSONified dictionary of these minimum, maximum, and average temperatures.

# Temperature Analysis I

# Temperature Analysis II
Presented with a hypothetical scenario where you are looking to take a trip from August first to August 2017, but are worried that the weather will be less than ideal. Using historical data in the dataset we find out what the temperature has previously looked like.

- Create a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
- Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").
- Plot the min, avg, and max temperature from your previous query as a bar chart.
- Use the average temperature as the bar height (y value) and use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

![image](https://user-images.githubusercontent.com/53978733/121992449-a9df9c00-cd6f-11eb-9815-871d3818b943.png)

## Daily Rainfall Average
Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!
- Calculate the rainfall per weather station using the previous year's matching dates.
- Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

## Daily Temperature Normals
- Calculate the daily normals across all weather stations for all previous years with matching month and day for your trip (August first to August seventh, inclusive). Normals are the averages for the min, avg, and max temperatures.
- Create a function called daily_normals that will return the daily normals for a specific month and day in tuple format. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.
- Use the daily_normals function to calculate the normals for each date string and append the resulting tuples to a list (so you will end up with a list of tuples).
- Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
- Plot an area plot (stacked=False) for the daily normals.

![image](https://user-images.githubusercontent.com/53978733/121992471-b2d06d80-cd6f-11eb-9407-9de322b6b024.png)



