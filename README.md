# DS3002_project1

The purpose of this project is to create an ETL pipeline using python and Docker.

The python file performs the following actions, in that order:

  1) Pulls from a remote data source and reads in a csv file from the specified user's directory
  2) Transforms the data by utilizing functions:
      - rename of columns
      - removal of columns
  3) Converts the data to the specified type, in this case .json
  4) Summarizes the output data
      - number of records
      - number of columns
      
 In my example for this project, I read in data from Kaggle - COVID-19's Impact on Airport Traffic.
 The dataset and more information can be found here: https://www.kaggle.com/terenceshin/covid19s-impact-on-airport-traffic?select=covid_impact_on_airport_traffic.csv
 
 When examining the data, I realized some of the labels needed to be simplified, along with some of the data not being very relevant.
 Due to this, I created the column rename/removal functions. This pipeline would be great to use in the future if more datasets with the same 
 information from the following year (2021 - 2022) is made available. The pipeline would allow for the same functions to take place simultaneously.
