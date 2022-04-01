import pandas as pd

#concentrate two dataframes
l1 = [
    ['john', 25, 'student'],
    ['mi', 24, 'student'],
    ['ma', 25, 'student'],
]
l2 = [
    ['mm', 25, 'student'],
    ['dd', 24, 'developer'],
    ['gg', 25, 'no'],
]
l3 = [
    ['jo', 25, 'teacher'],
    ['mo', 24, 'student'],
    ['to', 25, 'developer'],
]
l4 = [
    ['U.S'],
    ['U.K'],
    ['Korea'],
]
column_name = ['name', 'age', 'job']
df1 = pd.DataFrame.from_records(l1, columns=column_name)
df2 = pd.DataFrame.from_records(l2, columns=column_name)
print(df1)

result = pd.concat([df1, df2], ignore_index=True)
print(result)

result = df1.append(df2, ignore_index=True) # 이거 사라짐
print(result)

df3 = pd.DataFrame.from_records(l3, columns=column_name)
df4 = pd.DataFrame.from_records(l4, columns=['country'])
print(df4)

result = pd.concat([df3, df4], axis=1, ignore_index=True)
print(result)

label = [1, 2, 3, 4, 5]
prediction = [1, 2, 2, 4, 4]
comparison = pd.DataFrame({'label': label, 'prediction': prediction})
print(comparison)