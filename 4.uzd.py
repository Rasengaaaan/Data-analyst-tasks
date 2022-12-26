import pandas as pd
import columns as col

excel_file_path= 'C:/Users/Windows 10/Desktop/report_usage_data.csv'
df = pd.read_csv(excel_file_path)

only_date=pd.to_datetime(df[col.access]).dt.date
groupedIndex= df.groupby(only_date)
print(df[col.status].value_counts())
