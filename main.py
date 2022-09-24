import numpy as np
import pandas
import random
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib
from yellowbrick.classifier import ClassificationReport, ConfusionMatrix
import warnings
from sklearn.linear_model import LogisticRegression
warnings.simplefilter('ignore')


training_attributes = [' Idle Min', ' Idle Max', ' Destination Port', ' Active Max',	' Active Min', ' Down/Up Ratio', 'FIN Flag Count',	 ' SYN Flag Count'	, ' RST Flag Count'	, ' PSH Flag Count'	, ' ACK Flag Count'	, ' URG Flag Count'	, ' CWE Flag Count',	 ' ECE Flag Count' , ' Min Packet Length'	 ,' Max Packet Length' , ' Flow Duration'	, ' Total Fwd Packets'	, ' Total Backward Packets',	'Total Length of Fwd Packets'	, ' Total Length of Bwd Packets']

print(training_attributes, len(training_attributes))

dataset = pandas.read_csv("E:\MachineLearningCVE\Wednesday-workingHours.pcap_ISCX.csv", header=0)
anomalies = dataset[dataset[' Label'] == 'Web Attack']



"""
RFC = RandomForestClassifier(n_estimators=150, n_jobs=-1)


X, y = np.array(dataset[training_attributes]), np.array(dataset[' Label'])

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, train_size=0.75, shuffle=True)

RFC = joblib.load("modelNet.joblib")

visualizer = ClassificationReport(RFC, classes=['BENIGN', 'Anomaly'], support='count', is_fitted=True, cmap='RdBu')
visualizer.score(X_test, Y_test)
visualizer.finalize()
visualizer.show(outpath='ClassReportNet.pdf', clear_figure=True)

cm = ConfusionMatrix(RFC, classes=['BENIGN', 'Anomaly'], support='count', is_fitted=True, cmap='RdBu')
cm.score(X_test, Y_test)
cm.finalize()
cm.show(outpath='ConfMatrixNet.pdf', clear_figure=True)
predictions = RFC.predict(dataset[training_attributes])
print(predictions[80056])
"""
"""
#Commented out the previous part since the model has already been trained
dataset = pandas.read_csv("E:\MachineLearningCVE\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv", header=0)
RFC = RandomForestClassifier(n_estimators=150, n_jobs=-1)
X, y = np.array(dataset[training_attributes]), np.array(dataset[' Label'])

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, train_size=0.75, shuffle=True)

RFC = joblib.load("modelData.joblib")


print(dataset.head())
visualizer = ClassificationReport(RFC, classes=['BENIGN', 'Anomaly'], support='count', is_fitted=True, cmap='RdBu')
visualizer.score(X_test, Y_test)
visualizer.finalize()
visualizer.show(outpath='ClassReportData.pdf', clear_figure=True)

cm = ConfusionMatrix(RFC, classes=['BENIGN', 'Anomaly'], support='count', is_fitted=True, cmap='RdBu')
cm.score(X_test, Y_test)
cm.finalize()
cm.show(outpath='ConfMatrixData.pdf', clear_figure=True)


"""


def score(X):
    flow_duration = X[' Flow Duration']
    idle_min = X[' Idle Min']
    idle_max = X[' Idle Max']
    delta_idle = idle_max - idle_min
    ttl_fwd_packet = X[' Total Fwd Packets']
    ttl_bck_packets = X[' Total Backward Packets']
    delta_packts = ttl_fwd_packet - ttl_bck_packets
    ttl_len_bck_packets = X[' Total Length of Bwd Packets']
    return flow_duration * ttl_len_bck_packets + (delta_idle) + delta_packts 

anomaly_scores = list()
f = open("anomaly_scores.csv", "w")
f.write(f"' Flow Duration', ' Idle Min', ' Idle Max', ' Total Fwd Packets',' Total Backward Packets', ' Total Length of Bwd Packets', Score\n")

for i in range(len(anomalies)):
    X = anomalies.iloc[i]
    s = score(X)
    anomaly_scores.append(s)
    f.write(f"{X[' Flow Duration']}, {X[' Idle Min']}, {X[' Idle Max']}, {X[' Total Fwd Packets']}, {X[' Total Backward Packets']}, {X[' Total Length of Bwd Packets']}, {s}\n")
f.close()
print(max(anomaly_scores), min(anomaly_scores))