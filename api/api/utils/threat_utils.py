import pandas as pd
import random
from math import log, ceil

def get_anomalies():
    anomalies = pd.read_csv('./data/anomaly_scores.csv', header=0).to_dict('records')

    # convert score to scale of 1-10
    for a in anomalies:
        if a['score'] > 0:
            a['score'] = ceil(log(a['score'], 100))
        elif a['score'] < 0:
            a['score'] = 0
    
    # choose 100 random anomalies
    return random.sample(anomalies, 100)
