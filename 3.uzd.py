import pandas as pd
import numpy as np
import columns as col
import matplotlib.pyplot as plt

excel_file_path= 'C:/Users/Windows 10/Desktop/report_usage_data.csv'
df = pd.read_csv(excel_file_path)

freq_paths = df[col.report].value_counts()
top_paths = freq_paths.nlargest(5)
print('Top 5 paths: \n', top_paths)

groupedByCookie = df.groupby([col.cookie])
User1 = groupedByCookie.get_group('CHKXG0307N')[col.report].value_counts()
print('CHKXG0307N \n',User1.nlargest(5))

User2 = groupedByCookie.get_group('RETEL5407B')[col.report].value_counts()
print('RETEL5407B \n',User2.nlargest(5))

User3 = groupedByCookie.get_group('UUDPY8767A')[col.report].value_counts()
print('UUDPY8767A \n',User3.nlargest(5))

User4 = groupedByCookie.get_group('QMMJI1483Z')[col.report].value_counts()
print('QMMJI1483Z \n',User4.nlargest(5))

User5 = groupedByCookie.get_group('VNRJF5989O')[col.report].value_counts()
print('VNRJF5989O \n',User5.nlargest(5))

height = [top_paths[0], top_paths[1], top_paths[2], top_paths[3], top_paths[4]]
bars = ('index.html', 'path_6/report_2', 'path_9/report_3', 'path_5/report_12', 'path_4/report_15')
y_pos = np.arange(len(bars))

plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.show()
