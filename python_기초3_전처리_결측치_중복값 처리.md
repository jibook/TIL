deli.head()
deli.info()

deli.describe()



이런걸로 데이터를 확인한 후 전처리



### 전처리 순서



df1.dropna(how='all')   # 모든 값이 NA인 행 제거

df1.dropna(thresh=2)    # NA 아닌 값이 최소 2개 이상이면 제거하지 않음, 실무에서 유용



df1.dropna(axis=1, how='all') # 특정 컬럼이 모두 NA로만 구성되어 있으면 해당 컬럼 제거

df1.dropna(subset=['C'])  # 'C'컬럼에 NA 있는 행 제거, 실무유용

df1.fillna(method='ffill')   # NA를 앞에 있는 변수 값으로 치환





### 중복값 처리

ss1 = Series([1,1,2,3,4])
ss1
ss1.unique()  # 유일한 값 확인

#array([1, 2, 3, 4], dtype=int64)



ss1.duplicated()    # 중복된 값 확인 (boolean으로 반환)

ss1.drop_duplicates()  # 중복 제거, 모든 컬럼의 값이 일치하는 행 제거



df3.drop_duplicates(subset=['A','B'])   # A, B 컬럼의 값이 일치하는 행 제거



df2.drop_duplicates()
'''
   A   B
0  1  10
2  3  30
3  4  40
'''
df2.drop_duplicates(keep='last')
'''
   A   B
1  1  10
2  3  30
3  4  40
'''