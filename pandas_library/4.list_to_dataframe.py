import pandas as pd

# 리스트를 이용하여 데이터프레임 만들때
friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df.head())

# 리스트를 이용하여 한번에 데이터를 만들때
friend_list = [
    ['name', ['john', 'jane']],
    ['job', ['student', 'teacher']],
    ['age', [25, 30]],
]
df = pd.DataFrame.from_items(friend_list) # from_items가 존재하지 않음
print(df.head())