# prediction/ml_model.py
from sklearn.linear_model import LogisticRegression
import numpy as np

# Dummy training data (replace with real dataset later)
# Columns: [attendance%, marks, income, distance, health, support]
X = np.array([
    [80, 75, 20000, 2, 1, 1],
    [60, 55, 15000, 5, 0, 0],
    [90, 85, 30000, 1, 1, 1],
    [50, 40, 10000, 10, 0, 0],
])
y = np.array([0, 1, 0, 1])  # 0 = Safe, 1 = High Risk

def get_trained_model():
    model = LogisticRegression()
    model.fit(X, y)
    return model
