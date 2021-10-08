import time
import pandas as pd
import requests
import numpy as np
import csv

def data_state():
    startTime = time.time()
    
    html2 = requests.get('https://github.com/wnarifin/covid-19-malaysia/blob/master/covid-19_my_state.csv').content
    df_list2 = pd.read_html(html2)
    df2 = df_list2[-1]
    last2 = df2.iloc[[-16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]]
    last2 = last2.drop(last2.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
    data = []
    data = last2.values.tolist()
    with open('state.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        headers = ['date','state','new_cases', 'total_cases', 'new_deaths', 'total_deaths']
        writer.writerow(headers)
    
        for dat in data:
            writer.writerow(dat)

    return None

data_state()
