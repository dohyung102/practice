import imp


import pandas as pd

# None값을 찾고 이를 원하는 값으로 변경
friend_list = [
    ['john', 25, 'student'],
    ['mi', 24, 'student'],
    ['ma', 25, 'student'],
    ['me', 27, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', None, 'developer'],
    ['nat', 31, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df.shape)
print(df.info())

print(df.isna())
print(df.isnull())

# df.age = df.age.fillna(0)
# print(df)

df['age'].fillna(df.groupby('job')['age'].transform('median'), inplace=True) # gropuby로 나온 값이 None일수도 있으니 조심
print(df)
