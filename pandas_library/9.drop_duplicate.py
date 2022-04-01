import pandas as pd

# 중복 행 제거
friend_list = [
    ['john', 25, 'student'],
    ['mi', 24, 'student'],
    ['ma', 25, 'student'],
    ['me', 27, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
    ['me', 27, 'student'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

print(df.duplicated()) # 중복 체크

print(df.drop_duplicates()) # 중복 제거

print(df.duplicated(['name']))

print(df.drop_duplicates(['name'], keep = 'last')) # 중복 제거 keep의 디폴트는 first, last는 처음값 삭제