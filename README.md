## Overview
This project focuses on analyzing temperature trends around Oahu, HI to aid in the development of a business proposal for a “Surf-‘n-Shake” shop on the island. Using weather data stored in a SQLite database, SQLAlchemy is used to query the database to create summary tables of statistical information about the weather during June and December *of the previous year[(1)](#notes). By comparing weather trends around the solstice and equinox, this project aims to explore how temperature trends are affected by the summer and winter months, and provide insight about the temperature as investment risks for the new business venture. 
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
The previous image shows the outcome of a query that instructed SQLAlchemy to fetch the data for every day of June 2021, and every day of December 2021. Between the first and last day of the month, June and December returned 1700 and 1517 data points respectively, meaning data points were recorded on average about 53 times a day. 

The results show that the average temperatures are very close to eachother, with June being slightly warmer than December on Average. This is a good indication the business will be set up for success; if summer, the quintessential time of year for outdoor activities, is on average a similar temperature as winter, the weather should be nice year round! This idea is reinforced by a small standard deviation. Because the standard deviation measures how far the data is spread from the average, and a smaller number indicates the temperature is in general close to the average. If plotted on a histogram, the data is consistent with these findings. 

![surfs_up](https://raw.githubusercontent.com/svujcich/surfs_up/main/Resources/temps_june_december.png)

Although the temperature data is generally in support of the buisness proposal, the minimum temperatures should also be considered. In December, temperatures reached a low of 56 degrees, compared to a low of 64 degrees in June. This suggests that cold days in December might be colder,  which could impact traffic if it is too cold for surfing (never too cold for ice cream!). When considering the minimum temperature, the first quartile temperature should also be taken into account. Even though the cold days might be colder, 25% of the data below the average is only a 2 degree differemce from the average, this sugests in general the cold days are not too much colder than the average. 
 
Another querys that might be helpful in painting a picture about weather patterns might include a query that returns average percipitation statistics for June and December. This information might provide insight into another adverse weather trend that has potential to affect the "Surf'n'Shake" buisness. It might also be useful to query all of the temperatues *from the previous year(1). Using Matplotlib, the results can be transformed into a line graph which would be helpful in visualizing the data over time. 

Click [here](https://www.youtube.com/watch?v=4-mGiIRBhsE&t=9s) for a video explination of how python can work with SQLalchemy to query a SQLlite database, and a demo of using Flask to display SQLalchemy query results in an html page. 

##### Notes
  (1) SQLite data provided is from 2017; "of previous year" outdated from 2022. Given a data set from 2021, results would be more relevant. 

