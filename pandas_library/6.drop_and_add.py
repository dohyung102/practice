import pandas as pd
import numpy as np

# Drop row or column
friend_dict_list = [
    {'age' : 25, 'job' : 'student'},
    {'age' : 30, 'job' : 'teacher'},
    {'age' : 30, 'job' : 'teacher'}
]

df = pd.DataFrame(friend_dict_list, index=['john', 'jane', 'nate'], columns=['age', 'job'])

print(df.drop(['john', 'nate'])) # 없애고 싶은 index의 이름 입력

print(df.drop(['john', 'nate'], inplace=True)) # index를 없애고 df에 저장
print(df)


friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

# index로 삭제
print(df.drop(df.index[[0, 2]]))

print(df[df.age > 25]) # 필터한걸 df에 저장하면 됨

print(df.drop('age', axis=1)) # 필터한걸 df에 저장하면 됨

df.drop('age', axis=1, inplace=True) # 필터한걸 df에 자동 저장
print(df)

#column 추가
friend_list = [
    ['john', 25, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 30, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
df['salary'] = 0
print(df)

df['salary'] = np.where(df['job'] != 'student', 'yes', 'no')
print(df)

friend_list = [
    ['john', 95, 85],
    ['jane', 85, 80],
    ['nate', 30, 10],
]
column_name = ['name', 'midterm', 'finalterm']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df)

df['total'] = df['midterm'] + df['finalterm']
print(df)

df['avg'] = df['total'] / 2
print(df)

grades = []
for row in df['avg']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    else:
        grades.append('C')

df['grade'] = grades
print(df)

def pass_or_fail(row):
    if row != 'F':
        return 'pass'
    else:
        return 'fail'

df.grade = df.grade.apply(pass_or_fail) # 특성 함수를 적용하는법
print(df)

date_list = [
    {
        'yyyy-mm-dd' : '2000-06-27'
    },
    {
        'yyyy-mm-dd' : '2007-10-27'
    }
]
df = pd.DataFrame(date_list, columns= ['yyyy-mm-dd'])
print(df)

def extract_year(row):
    return row.split('-')[0]

df['year'] = df['yyyy-mm-dd'].apply(extract_year)
print(df)

# 데이터 합치기
friend_list = [
    ['john', 95, 85],
    ['jane', 85, 80],
    ['nate', 30, 10],
]
column_name = ['name', 'midterm', 'finalterm']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
df2 = pd.DataFrame([
    ['ben', 50, 50]
], columns = ['name', 'midterm', 'finalterm'])
print(df2)

# df.append(df2, ignore_index= True) # 이거 없어짐
df = pd.concat([df, df2], ignore_index= True)
print(df)