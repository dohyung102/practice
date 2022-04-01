import pandas as pd

# select, filter
friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

# index 범위로 필터링
print(df[1:3])

# 원하는 index로 필터링
print(df.loc[ [0, 2] ])

print(df[df.age >= 30])

print(df.query('age > 25'))

print(df[ (df.age>25) & (df.name == 'nate')])

# 컬럼으로 필터(컬럼명이 없을 때)
friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
]
df = pd.DataFrame.from_records(friend_list)

# 앞부분은 row index, 뒷부분은 column index
print(df.iloc[:, 0:2]) # :만 입력하면 처음부터 끝까지 다 보여줌

# 컬럼명으로 필터
df = pd.DataFrame.from_records(friend_list, columns=column_name)
df_filtered = df[['name', 'age']]
print(df_filtered)

print(df.filter(items=['age', 'job']))

print(df.filter(like='a', axis=1))

print(df.filter(regex='b$', axis=1))