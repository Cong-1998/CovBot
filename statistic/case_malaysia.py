import pandas as pd
import requests
import numpy as np
import csv

def data_malaysia():
    
    html = requests.get('https://github.com/wnarifin/covid-19-malaysia/blob/master/covid-19_my_full.csv').content
    df_list = pd.read_html(html)
    df = df_list[-1]
    df = df.drop(df.columns[[0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27,28, 29]], axis=1)
    last = df.iloc[[-1]]
    data = []
    data = last.values.tolist()
    with open('malaysia.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        headers = ['date','location','new_cases','new_deaths','total_cases','total_deaths','recover','total_recover']
        writer.writerow(headers)
    
        for dat in data:
            writer.writerow(dat)

    return None

data_malaysia()
