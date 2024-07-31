import numpy as np
import pandas as pd

data = pd.read_csv(
    "AIO-Homework/AIO-Module02-Week04-StatisticsExercise/advertising.csv")


def correlation(x, y):
     return np.corrcoef(x, y)[0, 1] # Lấy PT ở hàng 0 cột 1 của ma trận trả về bởi np.corrcoef


x = data['TV']
y = data['Radio']

corr_xy = correlation(x, y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
            corr_xy = correlation(data[feature_1], data[feature_2])
            print(f"Correlation between {feature_1} and {feature_2}: {round(corr_xy, 2)}")