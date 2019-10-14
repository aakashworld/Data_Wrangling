# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 05:30:02 2019
@author: Aakash Raj
"""

import pandas
import pandasql

filename = 'A:\DataScience\Intro_to_DS\weather-underground.csv'
weather_data = pandas.read_csv(filename)

q = """
SELECT count(*) from weather_data WHERE rain = 1;
"""
    
 #Execute your SQL command against the pandas frame
rainy_days = pandasql.sqldf(q.lower(), locals())
print(rainy_days)
    