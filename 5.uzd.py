import pandas as pd
import columns as col
import plotly.graph_objects as go

excel_file_path= 'C:/Users/Windows 10/Desktop/report_usage_data.csv'
df = pd.read_csv(excel_file_path)

df['only_date']=pd.to_datetime(df[col.access]).dt.date
list_bydates=list(df[col.host].groupby(df['only_date']))
print(list_bydates)
chart_data= [go.Bar( x=df['only_date'],y=df[col.host],marker=dict(color='Yellow'))]
figure = go.Figure(chart_data)
figure.show()

no_request=df[col.referer].value_counts()

print(no_request)