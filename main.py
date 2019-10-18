import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read data
submissions_data=pd.read_csv('submissions_data_train.csv')
event_data=pd.read_csv('event_data_train.csv')

"""
#data struct
event:
step_id
user_id
timestamp
action: discovered, viewed, started_attempt, passed

submission:
step_id
timestamp
submission_status
user_id

"""
#task1: find course mentor id
#find who was the first one to solve some step
#picking the first step mentioned
step_ = event_data['step_id'][0]
d = event_data[event_data.step_id== step_]
d=d[d.action=='passed']
d['date'] = pd.to_datetime(d.timestamp, unit='s')
time = d.date.min()
mentor=d.loc[(d['date']==time)].user_id
print(mentor)
#find who got most correct submissions
d=submissions_data[submissions_data.submission_status == 'correct'].groupby('user_id').agg({'submission_status': 'count'}).sort_values(by=['submission_status'], ascending=False)

print(d)