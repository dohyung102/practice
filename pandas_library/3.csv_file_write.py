import pandas as pd

# 데이터를 csv파일로 저장하는 방법
friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df.head())

df.to_csv('friends.csv')
df.to_csv('friends.csv', index=True, header=True) # index, header는 기본값으로 true index: 인덱스 유무
df.to_csv('friends.csv', index=True, header=True, na_rep = '-') # na_rep은 None데이터를 -으로 저장
