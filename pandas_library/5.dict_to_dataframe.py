import pandas as pd
from collections import OrderedDict

friend_dict_list = [
    {'name' : 'john', 'age' : 25, 'job' : 'student'},
    {'name' : 'jane', 'age' : 30, 'job' : 'teacher'}
]
df = pd.DataFrame(friend_dict_list)
print(df.head())

# 정렬된 dict를 쓰고싶을때
friend_ordered_dict = OrderedDict(
    [
        ('name', ['john', 'jane']),
        ('job', ['student', 'teacher']),
        ('age', [25, 30]),
    ]
)
df = pd.DataFrame.from_dict(friend_ordered_dict)
print(df.head())
