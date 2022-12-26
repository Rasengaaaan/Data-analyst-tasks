import pandas as pd
import columns as col

excel_file_path= 'C:/Users/Windows 10/Desktop/report_usage_data.csv'
df = pd.read_csv(excel_file_path)

id_max= df.loc[df[col.up_time].idxmax(), col.report]
max_path = df[col.up_time].max()
print("Max upload time is: " + id_max,max_path)

groupedByHostname = df.groupby([col.report])
for name,group in groupedByHostname:
    print("Median: " + name, group[col.up_time].median())

