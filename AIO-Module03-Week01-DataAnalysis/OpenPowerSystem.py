import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset_path = 'AIO-Homework/AIO-Module03-Week01-DataAnalysis/Dataset/opsd_germany_daily.csv'

data = pd.read_csv(dataset_path)

# print(data.shape)
data = data.set_index('Date')
# print(data.head())
data = pd.read_csv(dataset_path, index_col=0, parse_dates=True)

data['Year'] = data.index.year
data['Month'] = data.index.month
data['Weekday Name'] = data.index.day_name()
# Display random sampling 5 rows
# print(data.sample(5, random_state=0))

print(data.loc['2014-01-20':'2014-01-22'])

# Visualize the Consumption
# if 'Consumption' in data.columns:
#     # Cài đặt kích thước hình với Seaborn
#     sns.set(rc={'figure.figsize': (11, 4)})

#     # Vẽ biểu đồ mức tiêu thụ với Pandas và Matplotlib
#     plt.plot(data['Consumption'], linewidth=0.5)
#     plt.title('Consumption Over Time')
#     plt.xlabel('Time')
#     plt.ylabel('Consumption')
#     plt.show()
# else:
#     print("Column 'Consumption' does not exist in the dataframe.")

# Visualize some row
# cols_plot = ['Consumption', 'Solar', 'Wind']
# axes = data[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
# for ax in axes:
#     ax.set_ylabel('Daily Totals (GWh)')
# plt.show()

times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
consum_sample = data.loc[times_sample, ['Consumption']].copy()
print(consum_sample)

# Forward filling for missing_values
consum_freq = consum_sample.asfreq('D')
consum_freq['Consumption - Forward Fill'] = consum_sample.asfreq('D', method='ffill')
print(consum_freq)