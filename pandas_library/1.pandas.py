import pandas as pd

# pandas의 2가지 데이터 형식
# Series
data = [1, 2, 3]
s = pd.Series(data)
print(s)


# Dadaframe
data = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}
 
df = pd.DataFrame(data)
print(df)

# Panel
# 1.2 버전부터 panel이 사라졌다고 함.
# data = np.random.rand(2, 3, 4)
