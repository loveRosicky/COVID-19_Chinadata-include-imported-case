# -*- coding: utf-8 -*-
"""
@author: Jiayun loveRosicky
"""
import json

import pandas as pd

with open('area_trend_chart_data999.json','r',encoding='utf-8') as f :
  
  totallist_data=json.load(f)['data']
  

title=totallist_data[0].keys()


pd.DataFrame(totallist_data,columns=title).to_csv('covid_histdata.csv')