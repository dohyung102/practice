import pandas as pd
import numpy as np

# map, applymap
date_list = [
    {
        'date' : '2000-06-27'
    },
    {
        'date' : '2007-10-27'
    },
    {
        'date' : '2005-12-20'
    }
]
df = pd.DataFrame(date_list, columns= ['date'])
print(df)

def extract_year(date):
    return date.split('-')[0]

df['year'] = df['date'].map(extract_year)
print(df)

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
df.job = df.job.map({'student': 1, 'developer': 2, 'teacher': 3})
print(df)

friend_list = [
    [1.1, 25, 5.2],
    [1.1, 25, 5.2],
    [1.1, 25, 5.2],
]
column_name = ['x', 'y', 'z']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
df = df.applymap(np.around) # 모든 컬럼에 적용하고 싶을 때
print(df)