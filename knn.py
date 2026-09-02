import pandas as pd
import math
from collections import Counter

data = pd.read_csv(r"C:\Users\MY-PC\Downloads\health_data_1000.csv")
X = data[['blood_pressure', 'cholesterol']].values.tolist()
y = data['stroke'].tolist()


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def knn_predict(X_train, y_train, x_new, k=5):
    distances = []

    for i, x in enumerate(X_train):
        dist = distance(x, x_new)
        distances.append((dist, y_train[i]))

    distances.sort(key=lambda x: x[0])

    neighbors = [label for (_, label) in distances[:k]]
    vote = Counter(neighbors)
    return vote.most_common(1)[0][0]


bp = float(input("Enter blood pressure: "))
chol = float(input("Enter cholesterol: "))

new_sample = [bp, chol]

prediction = knn_predict(X, y, new_sample, k=5)

print(f"Prediction: {prediction} (1=stroke, 0=no stroke)")