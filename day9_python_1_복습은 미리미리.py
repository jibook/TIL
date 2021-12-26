# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:15:25 2021

@author: jhjh3
"""


### python_1_변수와 리스트


vsum = 1
vsum

v1 = 'abcd'
v1

v2 = round(1.5) # 반올림
v2

# 1) 모듈 호출 : 하위함수 (모듈명, 함수명)
import math
import math as ma  # as : alias 별칭

ma.trunc(1.5) # 내림

# 2) 모듈 내 함수 직접 호출 : 함수명만 사용 가능
from math import trunc # math 모듈 중에 trunc만 호출해서 사용
trunc(1.5)
trunc(1.7)

3+2
3/1.5
10-2
5*3
5**3 # 제곱
9//2 # 몫
9%2  # 나머지

ma.pow(3,2) # 3의 제곱

# 1. 리스트 생성
l1 = [1,2,3,4]
l1
type(l1)
l2 = [1,2,3,'4']
type(l2)
type(['4'])

t1 = (1,2,3,4)  # tuple : 상수 (변하지 않는 값 -> 변경이 불가능한 값)
type(t1)
t2 = 1,2,3,4


# 2. 색인
l1[-3]   # 2
l1[1:3]  # n:m --> n부터 m-1 까지

# l2[0,2] : 불가, 여러 숫자 전달 불가 ,말고 :

l1[0]=10  # 수정가능

# 3. 연산
l1 + 1 # 리스트와 정수(int) 연산 불가
l1 > 1 # 조건 전달 불가

[1,2,3]+[10,20,30]  # [1, 2, 3, 10, 20, 30]

l1 + [5]  # [10, 2, 3, 4, 5]

l1.append(6)
l1  # [10, 2, 3, 4, 6]

# 문자열 더하고 곱하기
'a' + 'b'
'a'*3

# 튜풀(상수) 수정
t1

t1[0]=10
# 튜풀(상수)는 수정이 안댐 

# 4. 삭제
del(l1[0])
l1
del(l1) # 객체 삭제
l1

# 리스트 내 모든 원소 삭제
l2 = []
l2 

# 함수(function)와 메서드(method)
# 메서드 : 함수의 일부
# 인수 전달 방식이 다르다.

sum([1,2,3]) # 6 : 함수 : 인수 전달이 모두 괄호 안에서 진행

import numpy as np
a1 = np.array([1,2,3])
a1 # array([1, 2, 3])
a1.sum() #6

# 메서드 
# - 객체(object)에서 호출 가능한 형태의 함수
# - 값을 객체가 가지고 있어요


### python_2_변수와 리스트

# 함수와 매서드
# 함수 : 함수(대상)
# 매서드 : 대상, 매서드

v1 = 'abcde'       # 문자(string)
v1.upper()         # 대문자 치환
v1.lower()         # 소문자 치환
'abc def'.title()  # camel 표기법 (단어의 첫글자만 대문자로 표시)

'abcd'[0]
'abcd'[0:2]

# ex) '031)345-0834'에서 지역번호만 추출
vtel = '031)345-0834'
vtel[0:3]

# 문자열의 시작, 끝 여부 확인
# v1.startswith(prefix,    #시작값 확인 문자
#               start,     #확인할 시작 위치
#               end,)      #확인할 끝 위치

v1
v1.startswith('b')      # False
v1.startswith('b',1)    # True
v1[1:].startswith('b')  # True

v1
v1.endswith('e')        # True
v1.endswith('E')        # False


# 앞뒤 공백
'abc' == 'abc'
'   abc   '.strip()    # 'abc'
'abc'.strip('a')       # 'bc'
'abcab'.strip('a')     # 'bcab'  중간 글자는 삭제 안해줌

'  abcd  '.lstrip()      #왼쪽 공백 또는 글자를 없애줌
'  abcd  '.rstrip()      #오른쪽 공백 또는 글자를 없애줌

# 치환
# 'abcabc'.replace(old,   #찾을 문자열
#                  new)   #바꿀 문자열

'abcdesd'.replace('a','A')
'abcadaedags'.replace('a','') 
'bcadaedagsa'.strip('a') # 'bcadaedags' : 양끝에 있는 'a'만 제거해줌
'bcadaedagsa'.strip('e')

# 문자열 분리
# v1.split(sep) #분리 구분기
'a/b/c/d'.strip('/')
'a/b/c/d'.strip('/')[1]
'a/b/c/d'.strip('/')[0:2]

# 위치값 리턴
# 'abcd'.find(sub,       #위치값을 찾을 대상
#             start,     #찾을 위치(시작점)
#             end)       ##찾을 위치(끝)점

v1
v1.find('b')

# ex. 전화번호에서 지역번호 추출하려고 해요 
#')'위치를 확인해서 그 이전까지 추출하세요

vnum=vtel.find(')')
vtel[0:vnum]
vtel[:vnum]

# 포함 횟수
'abcabcabc'.count('a')

# 형(type) 확인
type(v1)       # str 문자 : 데이터 타입확인
v1.isalpha()   # 문자확인 : True
v1.isnumeric()   # 숫자확인 : False

# 대소문자 확인
v1.isupper()
v1.islower()

# 문자열 결합
'a' + 'b'  # 'ab'

# 문자열 길이
len(v1)   # 5
3/len(v1) # 0.6

# 연습해 볼까요?
vname='jhjh'
vemail='jhjh306@gmail.com'
jumin='960306-2222222'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1] == 'm'
vname[1] == 'h'

# 2. vemail에서 이메일 아이디만 추출
vemailid=vemail.find('@')
vid=vemail[:vemailid]
vid

# 3. 주민번호에서 여자인지 확인 (참고: 남자:1, 여자:2)
jumin.find('-')

list(jumin.split('-'))
jumin.split('-')       # ['960306', '2222222']
jumin.split('-')[0]    # '960306'   
jumin.split('-')[1]    # '2222222'   
jumin.split('-')[1][0] # '2'
list(jumin.split('-'))

jumin[7]  == '2'

