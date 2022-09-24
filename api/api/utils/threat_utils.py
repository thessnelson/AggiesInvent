import pandas as pd
from math import log, ceil

def get_anomalies():
    anomalies = pd.read_csv('./data/ExampleData.csv', header=0).to_dict('records')

    # convert score to scale of 1-10
    for a in anomalies:
        a['score'] = log(int(a['score']), 100)
    
    return anomalies
