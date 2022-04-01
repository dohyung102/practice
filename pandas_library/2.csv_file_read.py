import pandas as pd

# csv파일 가져오기
df = pd.read_csv('파일경로/파일명')
df.head() # 상위 몇개를 보여주는 메서드 빈값일시 5개
df.tail() # 하위 몇개를 보여주는 메서드

# ,가 아닌 다른 구분자로 구분되어 있을때
df = pd.read_csv('파일경로/파일명', delimiter='\t') # delimiter 추가

# 파일에 칼럼명이 없을경우
df = pd.read_csv('파일경로/파일명', header= None) # 칼럼명이 숫자로 들어감
df.columns = ['칼럼명1', '칼럼명2', '칼럼명3'] # 칼럼명 넣어주는 방법

df = pd.read_csv('파일경로/파일명', header= None, names= ['칼럼명1', '칼럼명2', '칼럼명3']) # 한번에 추가하는 방법