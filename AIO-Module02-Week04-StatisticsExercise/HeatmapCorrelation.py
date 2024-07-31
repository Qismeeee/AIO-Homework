import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(
    "AIO-Homework/AIO-Module02-Week04-StatisticsExercise/advertising.csv")

plt.figure(figsize=(10, 8))

result = data.corr()
sns.heatmap(result, annot=True, fmt=".2f", linewidth=.5)

plt.show()
