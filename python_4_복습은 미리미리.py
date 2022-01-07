# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:34:03 2021

@author: jhjh3
"""


# Pandas _ Series, DataFrame

# pandas : 2차원 정형데이터(테이블, 표, 데이터프레임)
# - 기본단위 : Series
# - 1차원 자료 구조
# - 하나의 데이터 타입 허용

s1 = Series([1,2,3,4])
s2 = Series([1,2,3,'4'])
s3 = Series([1,2,3,4], index =['a','b','c','d'])
s3

Series(s3, index=['A','B','C','D'])


# 색인 indexing
s2[2]
s1[0:1]     # 행 0부터 1-1까지
s1[[0,3]]   # 행 0이랑 3

s3['a']
s3['a':'c']    # 인덱스 a부터 c까지
s3[['a','c']]  # 인덱스 a이랑 c

s1>2
'''
0    False
1    False
2     True
3     True
dtype: bool
'''
s1[s1 > 2]
'''
2    3
3    4
dtype: int64
'''
s3.b     # 2 >>  key indexing


# 연산
s1+1   # 가능
s4=Series([10,20,30,40])
s5=Series([10,20,30,40], index=['c','d','e','f'])

s1+s4
s3+s5

s3.add(s5, fill_value=0)
# 있는건 더하고 없는건 0 취급해서 넣음. NA 반환 방지

s3.sub(s5, fill_value=0) # - 연산
s3.mul(s5, fill_value=1) # * 연산
s3.div(s5, fill_value=1) # / 연산


# 기본메소드
s1.dtype    # 데이터 타입
s1.index    # 인덱스 출력
s1.values   # 값 출력

s3[['c','d','a','b']]          # 색인 사용, 배치 순서 변경
s3.reindex(['c','d','a','b'])  # 매소드 사용, 배치 순서 변경
s3.reindex(['a','b','c','d'])

s3.index = ['A','B','C','D']   # index 수정
s3
s3[0] = 10   # 값 수정


# DataFrame
# 2차원 자료구조 (행과 열 구조)

# 생성
d1={'name':['smith','will'],'sal':[900,1800]}
d1

df1=DataFrame(d1)
df1

import numpy as np 

d3 = DataFrame(np.arange(1,7).reshape(2,3), index=['a','b'], columns=['col1','col2','col3'])
d3

np.arange(1,7).reshape(2,3)
'''
array([[1, 2, 3],
       [4, 5, 6]])
'''
#색인(indexing) ****

d3.col1
d3['col1']
'''
a    1
b    4
Name: col1, dtype: int32
'''


# iloc, loc ****
# iloc : positional indexing 숫자로 위치를 뽑아옴[행인덱스,열인덱스]
# loc(location) : label indexing 해당하는 행을 뽑아온다

d3
d3.loc['a']
d3.loc['a','col2']
d3.loc[:,['col1','col3']]
d3.iloc[:,0]
d3.iloc[:,[0,-1]]


# 조건색인 처리
d3.loc[d3.col1==1,:]


# 기본 매서드
d3
d3.dtypes # 각 컬럼 별 데이터 타입 확인
d3.index
d3.columns
d3.values

d3.columns=['A','B','C'] 


# 연산
d3 +10

d4=DataFrame({'A':[10,40],'B':[20,30],'C':[30,80]},index =['a','b'])
d5=DataFrame({'A':[10,40],'B':[20,30]},index =['a','b'])

d3
d3+d5
d3.add(d5, fill_value=0)




# Pandas 문자열 매소드
# 기본매소드 : 벡터 연산 불가능 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')[1]

l1 =['abc','def']
l2 =['a/b/c','d/e/f']

l1.upper()    #리스트는 안돼요 불가
l2.split()    #리스트는 안돼요 불가

list(map(lambda x: x.upper(),l1))
list(map(lambda x: x.split('/'),l2))


# pandas 매서드 : 백터화 내장 (매 원소마다 반복 가능)
# Series, DataFrame 적용 가능

from pandas import Series, DataFrame

# 1) split
Series(l1)

s1=Series(l1)
s2=Series(l2)
s1
s2

s2.split('/')      #안돼요 불가
s2.str.split('/')  #돼요 가능

# 대소치환
s1.str.upper()   #대문자 치환
s1.str.lower()   #소문자 치환 (***)
s1.str.title()
# 0    Abc
# 1    Def
# dtype: object


# replace (치환)
s1.str.replace('a','A')  #문자열 치환
s1.str.replace('a','')  #문자열 삭제


#[예제] 천단위 구분기호 처리

s3=Series(['1,200','3,000','4,000'])
s3.str.replace(',','')
'''
0    1200
1    3000
2    4000
dtype: object
'''
s3.str.replace(',','').astype(int)        # 객체에서 숫자로 바꿔줘야 합할 수 있지
s3.str.replace(',','').astype(int).sum()  # 더했다! 8200

# 패턴확인 : stratswith, endswith, contains (bool로 나옴 T/F)
s1
s1.str.startswith('a')

s1[s1.str.startswith('a')] 
s1[s1.str.endswith('c')]
s1[s1.str.contains('e')]


#문자열 크기 len()
s1.str.len() 


# count 포함되어 있는 개수
Series(['aabca','abcdsa']).str.count('a')


# 문자열 제거(제거함수 : 공백, 문자)
Series(['        cd    ','    df       ']).str.strip()
Series(['        cd    ','    df       ']).str.strip().str.len()


s1.str.strip('a')    #문자열 제거
Series(['aaabaaca','abcba']).str.strip('a')

Series(map(lambda x: x.replace('a',''),['aaabaaca','abcba']))
Series(['aaabaaca','abcba']).str.replace('a','')

# find: 위치값 리턴
s6=Series(['abc@abc.com','avcvdds@abc.com'])
s6.str.find('@')

# 문자열 색인(추출)
'abcded'[0:3] # 문자열 색인
s6[0:1]
s6.str[0:5] 


# [예제 - 이메일 아이디 추출]
s6=Series(['abc@abc.com','avcvdds@abc.com'])

s6.map(lambda x: x[:x.find('@')])
s6.map(lambda x: x[:x.find('@')])
list(s6.map(lambda x: x[:x.find('@')]))

s6id=s6.str.find('@')
list(map(lambda x,y: x[0:y],s6,s6id))



# 문자열 삽입 pad
# s1.str.pad(5,               # 총자리수
#           'left',           # 삽입할 방향
#           '!')              # 삽입할 글자
s1
s1.str.pad(5, 'left','!')

# 문자열 결합 cat
'a'+'b'    #'ab'
'a'*3      #'aaa'

ss4=Series(['abc','def','123'])
ss4.str.cat()    # 'abcdef123'
ss4.str.cat(sep='-')

ss5=Series([['a','b','c'],['d','e','f']])
'''
0    [a, b, c]
1    [d, e, f]
dtype: object
'''
ss5.str.join(sep='')
'''
0    abc
1    def
dtype: object
'''




