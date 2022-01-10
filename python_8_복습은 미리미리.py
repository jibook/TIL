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

# run my_modules

kimchi = pd.read_csv("./data/kimchi.csv",encoding='cp949')

# kimchi 데이터를 연도별, 제품별 수량의 총합

kimchi.groupby(['판매년도','제품'])['수량'].sum()
df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()

# 멀티인덱스
# 인덱스나 컬럼이 여러 레벨로 표현 
# 상위레벨 : 0, 하위레벨로 갈 수록 숫자 증가

df2=df1.unstack()    # long --> wide 행이 컬럼이 바뀐다 대각선을 기준으로 
df2.stack()   

df1.unstack(level=0) # 상위레벨(2013) : 행세 인덱스가 컬럼으로 간다
df1.unstack(level=1) 

df2.stack(level=0)  # 얜 똑같네


# pivot_table
# 교차표 작성

kimchi.pivot_table(index = '판매월',      # index 방향에 배치할 컬럼명
                   columns ='판매처',     # column 방향에 배치할 컬럼명
                   values ='수량',        # 교차표에 작성할 값을 갖는 컬럼명
                   aggfunc ='sum'         # 그룹 함수
                   )


# 예제 kimchi 데이터를 이용해서 연도별, 제품별, 판매금액의 총합을 교차표로 작성하세요
kimchi

kimchi.pivot_table(index = '판매년도', columns = "제품", values = "판매금액", aggfunc = "sum")
'''
제품           무김치        열무김치        총각김치
판매년도                                    
2013  3809133886  3416217894  4186789117
2014  4111403907  4392490590  5250364301
2015  5212738410  5859079408  7485159996
2016  6903506142  6627888927  6378374872
'''



# ------------------------------------------NA 결측치 처리, 중복값 제거 (왕중요)

# NA (결측치) 처리 
# 숫자형 NA (float type), 문자형 NA


# run my_modules

s1 = Series([1,2,3, np.nan])




















