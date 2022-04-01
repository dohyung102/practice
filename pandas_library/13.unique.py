import pandas as pd

# 각 컬럼의 유니크한 값을 보여줌
friend_list = [
    ['john', 25, 'student'],
    ['mi', 24, 'student'],
    ['ma', 25, 'student'],
    ['me', 27, 'student'],
    ['jane', 30, 'teacher'],
    ['nate', 34, 'developer'],
    ['nat', 31, 'developer'],
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)

print(df.job.unique())
print(df.job.value_counts())