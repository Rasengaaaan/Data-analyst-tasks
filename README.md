# Data-analyst-tasks 💻 
![acf](https://user-images.githubusercontent.com/83876027/209586367-2292b27e-8822-4383-9296-3f9c1311960e.gif)

**Task 1** ☝️

I have to make sure to choose a company's offer that is willing to buy the claim rights of a defaulted loan that has a high risk of not being paid back. That is willing to agree to a price which either makes the company profit, most likely smaller than the original loan, or makes the company break even. Even if those previously mention criteria are not fulfilled, it’s better to cut losses and opt for an offer which will make the company lose less money.

**Task 2** ✌️

Each task can be run through the command promt.

```
location of python.exe "location of the task .py file"
```
For example
```
D:/Python/python.exe "d:/assignment/3.uzd.py"
```
Before doing the second task, I assigned constants for easier access of code.
```
host= 'hostname'
report= 'report_path'
access= 'access_date'
up_time= 'upload_time'
bytes_send= 'bytes_send'
status= 'http_status_code'
agent= 'http_user_agent'
referer= 'http_referer'
cookie= 'cookie_ga'
```
❓ 1. Which report_paths have longest upload time (upload_time)? Do bytes_send correlates with
upload_time?

```
id_max= df.loc[df[col.up_time].idxmax(), col.report]
max_path = df[col.up_time].max()
print("Max upload time is: " + id_max,max_path)
```
![Maxupload](https://user-images.githubusercontent.com/83876027/209584979-a1a7db45-d53f-4b9c-84e9-7b25451b2764.png)

  - 🙋‍♂️ path_4/report_25 has the longest upload time, which is: 45.013s.
```
corr=(df[col.bytes_send].corr(df[col.up_time]))
```
![corr](https://user-images.githubusercontent.com/83876027/209586287-8e329d6e-2285-4403-95f8-6ec83e1fadd7.png)
  - 🙋‍♂️ There is a negative correlation between bytes_send and upload_time

❓ 3.	Find top 5 report_path (plot usage of those report_path over time). What are favourite reports of top 5 users?
```
freq_paths = df[col.report].value_counts()
top_paths = freq_paths.nlargest(5)
print(top_paths)
```
```
height = [top_paths[0], top_paths[1], top_paths[2], top_paths[3], top_paths[4]]
bars = ('index.html', 'path_6/report_2', 'path_9/report_3', 'path_5/report_12', 'path_4/report_15')
y_pos = np.arange(len(bars))

plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.show()
```
![top_paths](https://user-images.githubusercontent.com/83876027/209586460-447e9773-f0bd-406c-996b-dddb8352e3be.png)
![top_pathChart](https://user-images.githubusercontent.com/83876027/209586486-40fecd43-33d0-486b-b7a0-8f5376b807a5.png)
  - 🙋‍♂️ The top 5 Report paths are index.html, path_6/report_2, path_9/report_3, path_5/report_12, path_4/report_15.
```
freq_users = df[col.cookie].value_counts()
top_users = freq_users.nlargest(5)
print(top_users)
```
![top_users](https://user-images.githubusercontent.com/83876027/209586551-32b9b2e3-0f1a-419d-876d-58c47d8e9b5f.png)
  - 🙋‍♂️ The top 5 Users are CHKXG0307N, RETEL5407B, UUDPY8767A, QMMJI1483Z, VNRJF5989O
```
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
```
![user_fav](https://user-images.githubusercontent.com/83876027/209586584-7bbffc05-fa2a-4552-8d47-ccfb4a32b44d.png)
  - 🙋‍♂️ path_6/report_2, path_9/report_3 and path_5/report_12 seem to the most common for the top 5 users.

❓ 4.	http_status_code is good place to understand if servers are responds properly. Please analyse those over time and make comments about it.
```
only_date=pd.to_datetime(df[col.access]).dt.date
groupedIndex= df.groupby(only_date)
print(df[col.status].value_counts())
```
![responds](https://user-images.githubusercontent.com/83876027/209586693-bbb7ba08-6f90-46d2-af74-0bac0fa521c5.png)
- 🙋‍♂️ Most of the time the servers responded properly (200- 92144), but there were times when there was a Bad Gateway which resulted in a server error (502- 162).
❓ 5.	As those are two servers supporting one main webpage, find date when we switched between servers and most traffic of one server was send to another server. 

  a. Was this switch only once?
```
chart_data= [go.Bar( x=df['only_date'],y=df[col.host],marker=dict(color='Yellow'))]
figure = go.Figure(chart_data)
figure.show()
```
![chart1](https://user-images.githubusercontent.com/83876027/209586898-175b1d96-b256-4472-a0ce-390ebf60843d.png)

![chart2](https://user-images.githubusercontent.com/83876027/209586910-c0f7ff28-adaf-4e07-b2e7-0f3622b4051e.png)
- 🙋‍♂️ The switch appears to have happened twice, once on October 31st and once on December 25th.

b.	Was there any time when one of the servers didn’t get any requests?
```
print(df[col.referer].value_counts())
```
![request](https://user-images.githubusercontent.com/83876027/209586948-e517059f-fbce-4876-b298-bab3b9d6d4e1.png)
- 🙋‍♂️ There were 21711 times when the server didn't get any requests.
