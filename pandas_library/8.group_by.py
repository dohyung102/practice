import pandas as pd

# 그룹 바이
friend_list = [
    ['john', 25, 'student'],
    ['mi', 24, 'student'],
    ['ma', 25, 'student'],
    ['me', 27, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

groupby_job = df.groupby('job')
print(groupby_job.groups)

for name, group in groupby_job:
    print(name + '+' + str(len(group)))
    print(group)
    print()

df_job_cnt = pd.DataFrame( {'count' : groupby_job.size()}).reset_index()
print(df_job_cnt)