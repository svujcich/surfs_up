## Overview
This project focuses on analyzing temperature trends around Oahu, HI to aid in the development of a business proposal for a “Surf-‘n-Shake” shop on the island. Using weather data stored in a SQLite database, SQLAlchemy is used to query the database to create summary tables of statistical information about the weather during June and December *of the previous year(1). By comparing weather trends around the solstice and equinox, this project aims to explore how temperature trends are affected by the summer and winter months, and provide insight about the temperature as investment risks for the new business venture. 
## Results
From a similar sample size at opposite times of the year, the results show:

- The average temperatures were within 4 degrees of each other

    - The average temperature for June was 75 degrees
    - The average temperature for December was 71 degrees

-	The standard deviation is small, so the data is close to the average 

      -	The standard deviation for June Temperatures is 3 degrees
      -	The standard deviation for December is 4 degrees
-	The minimum temperature was colder in December

    -	The minimum temperature in June is 64 degrees
    -	The minimum temperature in December is 56 degrees

  
![surfs_up](https://user-images.githubusercontent.com/106559768/185224699-99ddf17c-bff0-4a34-b7f2-f900f48de9b5.png)

## Summary
The previous image shows the outcome of a query that instructed SQLAlchemy to fetch the data for every day of June 2021, and every day of December 2021. Between the first and last day of the month, June and December returned 1700 and 1517 data points respectively, meaning data points were recorded on average about 53 times a day. This is a compelling detail that supports the idea that this data set provide a solid foundation for this analysis.

The results show that the average temperatures are very close to eachother, with June being slightly warmer than December on Average. This is a good indication the business will be set up for success; if summer, the quintessential time of year for outdoor activities, is on average a similar temperature as winter, the weather should be nice year round! This idea is reinforced by the standard deviation. Because standard deviation measures how far the data is spread from the average, a smaller number indicates the data is close to the average. The results show the temperatures are generally within 3 or 4 degrees of the average. 




  (1) SQLite data provided is from 2017, "of previous year" outdated from 2022. Given a data set from 2021, results would be more relevant. 

