# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 16:16:40 2022

@author: jhjh3
"""

# 13. merge
# 13. merge vs. concat
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기  
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)

# run my_modules

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.arange(1,7)
np.arange(1,7).reshape(2,3)

DataFrame(np.arange(1,7).reshape(2,3),columns=['A','B','C'])
df1 = DataFrame(np.arange(1,7).reshape(2,3),columns=['A','B','C'])
df2=DataFrame(np.arange(10,61,10).reshape(2,3),columns=['A','B','C'])

# concat
pd.concat([df1,df2])
# 행결합 > 기본은 세로방향으로 합침
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 0  10  20  30
# 1  40  50  60

pd.concat([df1,df2], axis=0)
pd.concat([df1,df2], ignore_index=True)

emp = pd.read_csv('./data/emp.csv')
emp

DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석부']})
df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석부']})

# join 
# 두 데이터프레임(테이블) 참조조건 활용, 하나의 객체로 합치거나 데이터를 처리하는 행위
# merge가 두 데이터 프레임 조인을 수행, 등가 조건만을 사용하여 조인이 가능

# pd.merge(left,             # 첫번째 데이터프레임
#          right,            # 두번째 데이터프레임
#          how='inner',      # 조인 방법(default = 'inner' ), 기본값
#          on=,              # 조인하는 컬럼(컬럼명이 서로 같을 때) 
#          left_on=,         # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
#          right_on=)        # 두번째 데이터프레임 조인(컬럼명이 서로 다를 때)


pd.merge(emp, df_dept, on='deptno' )
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      4  grace      10  4200    인사부
# 3      3   ford      20  4300    총무부
# 4      6   king      20  4000    총무부
# 5      5  scott      30  4100  IT분석부

pd.merge(emp, df_dept, how="left", on='deptno')
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      3   ford      20  4300    총무부
# 3      4  grace      10  4200    인사부
# 4      5  scott      30  4100  IT분석부
# 5      6   king      20  4000    총무부


# outer join
DataFrame({'deptno':[10,20], 'dname':['인사총무부','IT분석팀']})
df_dept_new=DataFrame({'deptno':[10,20], 'dname':['인사총무부','IT분석팀']})

pd.merge(emp, df_dept_new, on='deptno') # 30번 부서원 생략
pd.merge(emp, df_dept_new, on='deptno', how='outer')

pd.merge(emp, df_dept_new, on='deptno', how='left')



# ------------------------------------------------ drop shift rename

# 1. drop
# - 특정 행, 컬럼 제거
# - 이름 전달

emp = pd.read_csv("./data/emp.csv")
emp


# scott 퇴사
emp.loc('ename'=={"scott"})

emp['ename']=='scott'   # 조건문
emp.loc[emp['ename']=='scott']   # scott 관련된 record

emp.loc[emp['ename']=='scott',:] 
emp.loc[~(emp['ename']=='scott'),:] 

emp.drop(4, axis=0)     # 행기준, 4번째 idx 제외


# shift
# - 행 또는 열을 이동
# - 전일자 대비 증감율


emp['sal']  # dtype: int64 정수
emp['sal'].shift()  #default : aixs=0 (행), dtype : float64 실수

# 예제) 다음 데이터프레임에서 전일자 대비 증감율 출력
s1 = Series([3000,3500,4200,2800,3600],
       index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
s1

s1.shift()
'''
Out[69]: 
2021/01/01       NaN
2021/01/02    3000.0
2021/01/03    3500.0
2021/01/04    4200.0
2021/01/05    2800.0
dtype: float64
'''

# 1월 2일 증감률 >> (3500-3000)/3000 
(s1-s1.shift())/s1.shift()*100
'''
2021/01/01          NaN
2021/01/02    16.666667
2021/01/03    20.000000
2021/01/04   -33.333333
2021/01/05    28.571429
dtype: float64
'''



# rename
emp.columns = ['emptno','ename','deptno','salary']

emp.rename({'salary':'sal','deptno':'dept_no'}, axis=1)
#    emptno  ename  dept_no   sal
# 0       1  smith       10  4000
# 1       2  allen       10  4500
# 2       3   ford       20  4300
# 3       4  grace       10  4200
# 4       5  scott       30  4100
# 5       6   king       20  4000



# 예제 emp 데이터에서 ename을 idx로 설정 후 scott 을 SCOTT 변경
emp
emp.set_index('ename')   # ename을 맨앞, 즉 인덱스로 설정

emp_1 = emp.set_index('ename')
emp_1.rename({'scott':'SCOTT'},axis=0)

# fallow 답안 
emp.set_index('ename').rename({'scott':'SCOTT'})

emp.index = emp['ename']
emp.rename({'scott':'SCOTT'}, axis = 0)
