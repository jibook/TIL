# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:23:16 2022

@author: jhjh3
"""

# 15. stack, unstack, pivot_table

# 자료구조(datatype) 형태
# - long type(tidy data)
# - 각 속성을 컬럼으로 표현

# 지점
# A
# B
# C

# - wide data(cross table : 교차표)
# - 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열함

#            A       B        C
# 판매량

# stack / unstack
# 1. stack
# wide ->> long

# 2. unstack
# long --> wide

run my_modules

kimchi = pd.read_csv("./data/kimchi.csv",encoding='cp949')

# kimchi 데이터를 연도별, 제품별 수량의 총합

kimchi.groupby(['판매년도','제품'])['수량'].sum()
df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()

# 멀티인덱스
# 인덱스나 컬럼이 여러 레벨로 표현 
# 상위레벨 : 0, 하위레벨로 갈 수록 숫자 증가

df2=df1.unstack()    # long --> wide 행이 컬럼이 바뀐다 대각선을 기준으로 
df2.stack()   





















