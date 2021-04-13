#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:15:56 2021

@author: brianwimmer
"""


import pandas as pd # load pandas as pd
import json
import os

# Remote Data Source
# make more generic to any csv
in_file = os.getenv('INPUT_FILE')
os.chdir('processing')
travel = pd.read_csv(in_file)

# travel = pd.read_csv('/Users/brianwimmer/Desktop/UVA/Spring 2021/DS 3002/covid_impact_on_airport_traffic.csv')

# Transforming Data

# List of labels to be renamed
new_col_names = {
    'Centroid': 'Coordinates',
    'AirportName': 'Airport',
    'PercentOfBaseline': 'YearOverYear',
    'ISO_3166_2': 'ISO'
}

def modify(travel, in_file):
    # Refactor the dataframe to be converted to JSON
    # rename labels
    for label in travel:
        if label in new_col_names:
            travel = travel.rename(columns = {label: new_col_names[label]})
        
 # List of columns to be removed           
delete = {
    'AggregationMethod',
    'Version',
    'Geography'}

def delete(travel, in_file):
    # Remove columns in the dataframe to be converted to JSON
    # delete columns
    for label in travel:
        if label in delete:
            travel = travel.drop(columns = {label: delete[label]})
            
# Converting Data=
def convert(travel, in_file):
       travel.to_json(r'output_file.json')
            
# Summary Data
print("This dataset has " + str(len(travel)) + " records.")
print("This dataset has " + str(len(travel.columns)) + " columns.")
