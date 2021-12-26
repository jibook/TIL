# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:01:25 2021

@author: jhjh3
"""

# 문자열 메서드 
# 문자열 처리와 관련된 메서드 

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)
'a/b/c'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]  # b

l1=['abc','def']
l2=['a/b/c','d/e/f']

l1.upper()  # list 불가
l2.split()  # list 불가

list(map(lambda x: x.upper(),l1))      #['ABC', 'DEF']
list(map(lambda x: x.split('/'),l2))   #[['a', 'b', 'c'], ['d', 'e', 'f']]

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame 

# 1) split 

from pandas import Series, DataFrame

l1  # ['abc', 'def']

Series(l1)
# 0    abc
# 1    def
# dtype: object

s1=Series(l1)

l2  # ['a/b/c', 'd/e/f']
Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object
s2=Series(l2)

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

# 대소치환
s1
s1.str.upper()
s1.str.lower()
s1.str.title()

# replace
s1.str.replace('a', 'A')
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a', '')
# 0     bc
# 1    def
# dtype: object

# 예제 - 천단위 구분기호 처리
s3=Series(['1,200','3,000','4,000'])
ss3=s3.str.replace(',', '')
sum(list(map(lambda x : int(x), ss3)))


# 4) 패턴 확인 : strartswith, endswith, contains
s1
# 0    abc
# 1    def
# dtype: object

s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool

s1[s1.str.startswith('a')]  #s1 각 원소에서 'a'로 시작하는 원소 추출
# 0    abc
# dtype: object
s1[s1.str.endswith('c')]   #s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')]   #s1 각 원소에서 'e'를 포함하는 원소 추출


# 문자열 크기 len()
s1.str.len()
# 0    3
# 1    3
# dtype: int64

# count 포함 개수
Series(['aabbbb','abcdadd']).str.count('a')
# 0    2
# 1    2
# dtype: int64

Series(['       cd      ','        df      '])
Series(['       cd      ','        df      ']).str.strip()
Series(['       cd      ','        df      ']).str.strip().str.len()

s1

s1.str.strip('a')
Series(['aabbbb','abcdadd']).str.strip('a')
# 0      bbbb
# 1    bcdadd
# dtype: object
Series(['aabbbb','abcdadd']).str.replace('a','')
# 0     bbbb
# 1    bcddd
# dtype: object

# find (위치값 return)
s3=Series(['abc@gmail.com','abcdef@gmail.com'])
s3.str.find('@')

# 이메일 아이디 추출
s4=Series(['drwill@naver.com','zzuyu@drwill.kr'])
ss4=s4.str.find('@')
ss4
list(map(lambda x,y: x[:y],s4,ss4))
# ['drwill', 'zzuyu']

s4.map(lambda x : x[:x.find('@')])


#pad : 문자열 삽입
# s1.str.pad(5,           #총 자리수
#            'Left',      #삽입 방향
#            '!')         #삽입 글자


s1.str.pad(5,'left','!')
s1.str.pad(5, 'right', '?')

s5=Series(['i love u','you know'])
s5
s5.str.pad(20, 'right','^')


'a'+'b'
'a'*3

s6=Series(['abc','def','123'])
s6.str.cat()   # 'abcdef123'
s6.str.cat(sep=(','))  #'abc,def,123'
s6.str.cat(sep=('/'))  #'abc/def/123'


s7=Series([['a','b','c'],['d','e','f']])
s7
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

s7.str.join(sep='')       #Series 내 각 원소 내부의 문자열을 결합(공백)
# 0    abc
# 1    def
# dtype: object

s7.str.join(sep=',')       #Series 내 각 원소 내부의 문자열을 결합(,)
# 0    a,b,c
# 1    d,e,f
# dtype: object

s8 = Series(['a','b','c'],index=['d','e','f'])
s8 = Series(['a','b','c'],['d','e','f'])
s8
# d    a
# e    b
# f    c
# dtype: object

Series(['a','b','c'],index = ['drwill','zzuyu','hyory'])
Series(['a','b','c'],['drwill','zzuyu','hyory'])
Series(['a','b','c'],['x','y','z'])
