# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:07:16 2021

@author: jhjh3
"""

# run my_modules
from pandas import Series, DataFrame
import numpy as np

df1= DataFrame(np.arange(1,17).reshape(4,4))
df1
dir(df1)

df1.sum(axis=0)
df1.sum(axis=1)

df1.iloc[:,0]
df1.iloc[:,0].sum()
df1.iloc[:,0].mean()


df1.iloc[0,0] = np.nan
df1
'''
      0   1   2   3
0   NaN   2   3   4
1   5.0   6   7   8
2   9.0  10  11  12
3  13.0  14  15  16
'''
df1.iloc[:,0].mean()   # 9 없는건 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0].isnull()   # 조건(boolean)
df1
df1.iloc[:,0][df1.iloc[:,0].isnull()]=df1.iloc[:,0].mean()
df1
'''
      0   1   2   3
0   9.0   2   3   4
1   5.0   6   7   8
2   9.0  10  11  12
3  13.0  14  15  16
'''
df1.isnull()
df1[df1.notnull()] 
df1[df1.isnull()]  # 데이터프레임 전체에서 NaN 값 확인
#     0   1   2   3
# 0 NaN NaN NaN NaN
# 1 NaN NaN NaN NaN
# 2 NaN NaN NaN NaN
# 3 NaN NaN NaN NaN

df1.iloc[:,0].var()   # 10.66666666666666 >> 분산
df1.iloc[:,0].std()   # 3.265986323710904 >> 표준편차
df1.iloc[:,0].min()   # 5.0 >> 최솟값
df1.iloc[:,0].max()   # 13.0 >> 최댓값
df1.iloc[:,0].median() # 9.0 >> 중위수(중앙값)

round(df1.iloc[:,0].var(),2)






# replace 매서드_치환, 삭제

# replace 매서드
# 치환(찾을 문자열, 바꿀 문자열)

# 1. 기본 문자열 매서드
# - 기본 파이썬 제공
# - 문자열에서 호출 가능
# - 백터 연산(각 원소별 반복 처리 불가)
# - 오직 문자열 치환만 가능(숫자치환, NA 치환 불가능)

'abcd'.replace('a', 'A') # 'Abcd' >> a를 A로 치환
'abcd'.replace('a', '')  # 'abcd' >> 공백으로 치환
# 'abcd'.replace(1, '')
# TypeError: replace() argument 1 must be str, not int >> 숫자는 치환 안된다
# ' bcd'.replace('',1)
# TypeError: replace() argument 2 must be str, not int >> 숫자로 치환하는거안된다
# ['abcd','abcde','aabb'].replace(',','')


# for 문 활용
outlist=[]
for i in ['abcd','abcde','aabb']:
    outlist.append(i.replace('a','A'))
print(outlist)
# ['Abcd', 'Abcde', 'AAbb']

# map 활용
f1 = lambda x : x.replace('a','A')
list(map(f1,['abcd','abcde','aabb']))
# ['Abcd', 'Abcde', 'AAbb']

['abcd','abcde','aabb'].map(f1)
fff=Series(['abcd','abcde','aabb'])
fff.map(f1)
# Series는 map을 할 수 있고, list는 map을 할 수 없다.

Series(['abcd','abcde','aaaab',np.nan]).map (lambda x: x.replace(np.nan,''))
# TypeError: replace() argument 1 must be str, not float
# 문자열(str)이여야 함, NaN이 있으면 안돼
# 0     abcd
# 1    abcde
# 2    aaaab
# 3      NaN
# dtype: object




# 2. str.replace
# - pandas 제공 (Series 객체만 호출 가능)
# - 백터화 내장된 문자열 매서드
# - 문자열 호출 가능
# - 백터 연산(각 원소별 반복 처리) 가능
# - 오직 문자열 치환만 가능(숫자 치환, NA 치환 불가)
# - 숫자로 구성된 Series 적용 불가

Series(['abcd','abcde','aaaab']).str.replace('a', 'A')
# list, DataFrame 안되고 Series만 된다


# pandas replace
# - pandas 제공
# - 값 치환 메서드(똑같은 , 완전히 일치하는 값을 다른 값으로 대체, 삭제 )
# - Series, DataFrame 호출 가능 
# - 숫자, NaN 치환 가능 
# - 동시에 여러 대상 수정 가능


df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
df1
df1.replace(',','')  # 변화 없음 ','로 생긴 값을 삭제하는 의미

df2 = DataFrame([['1,200',','],['1,400','1,500']])
df2
df2.replace(',','')

df3 = DataFrame([['1200','1300'],['1400','.']], columns =['a','b'])
df3
df3.replace('.', np.nan)  # '.' 와 완전히 일치하는 값은 NaN 치환
df3.replace(['.','1400','?','!'], np.nan) 
#       a     b
# 0  1200  1300
# 1   NaN   NaN



# [연습 문제]
# df1에 천단위 구분기호 제거 후 모두 숫자 변경
df1
# edf1= lambda x : x.find(',')
# list(map())
# df1.DataFrame(find(','))     틀린거 연습해봐 더 
edf1=lambda x: x.find(',')

df1.applymap(lambda x : int(x.replace(',','')))


df1.applymap(lambda x : int(x.replace(',',''))).sum()

# 동료 코드1
copy_df1=df1
for i in range(0,len(df1)):
    copy_df1[i]=df1[i].str.replace(',','')
print(copy_df1)

# 동료 코드2
df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
for i in range(len(df1)):
    if df1[i].all() != 'int':
        df1[i] = df1[i].str.replace(',','').astype('int')
    else:
        pass
print(df1)
