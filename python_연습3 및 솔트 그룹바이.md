## sort() 정렬

1. sort_index

- Series, DataFrame() 호출 가능
- index, column 재배치

```python
데이터명.sort_index()   # 오름차순 디폴트값

데이터명.sort_index(ascending=True)  # 오름차순 
데이터명.sort_index(ascending=False) # 내림차순
```



2. sort_values

- Series ,DataFrame 호출 가능

- 본문의 값(value)으로 정렬 (Series, DataFrame 특정 칼럼 순서대로)

```python
데이터명.sort_values(by='컬럼명') # '컬럼명'으로 정리, 오름차순 디폴트값
# by 생략가능

데이터명.sort_values('컬럼명', ascending=True)  # 오름차순
데이터명.sort_values('컬럼명', ascending=False)  # 내림차순

emp.sort_values(by=['deptno','sal'],ascending=[True,False])
# 부서는 오름차순(가나다순), 연봉은 내림차순(큰순서)
```





## groupby 

- python pandas proupby
- 그룹연산
- 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
- groupby 매서드 처리 기능

```python
kimchi.groupby(by=None,  # 그룹핑 할 컬럼(기준)
               axis= 0,  # 그룹핑 연산 방향
               level = None) # 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용
```



```py
# 예제) 제품별, 판매처 별(김치별)
kimchi.groupby(by=['제품','판매처']).sum()
```

​        판매년도  판매월       수량         판매금액

제품   판매처                                   
무김치  대형마트  96696  312  1550027  14243851204
     백화점   96696  312   510114   5675796839
     편의점   96696  312    82623    117134302
열무김치 대형마트  96696  312  1491864  14272706507
     백화점   96696  312   567129   5897836502
     편의점   96696  312    89006    125133810
총각김치 대형마트  96696  312  1649486  16512153282
     백화점   96696  312   658442   6639524485
     편의점   96696  312   103725    149010519



```python
# 제품기준, 수량과 판매금액 총합 구하기
kimchi.groupby(by=['제품'])['수량','판매금액'].sum()
```

​       수량         판매금액

제품                        
무김치   2142764  20036782345
열무김치  2147999  20295676819
총각김치  2411653  23300688286



##### 멀티 인덱스

```python
# 예제) 제품별, 반매처별(김치별) 수량 총합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].sum()
kimchi.groupby(by=['제품','판매처'])['수량'].mean()

kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])
```

​           sum          mean

제품   판매처                        
무김치  대형마트  1550027  32292.229167
     백화점    510114  10627.375000
     편의점     82623   1721.312500
열무김치 대형마트  1491864  31080.500000
     백화점    567129  11815.187500
     편의점     89006   1854.291667
총각김치 대형마트  1649486  34364.291667
     백화점    658442  13717.541667
     편의점    103725   2160.937500



**agg** : 여러 함수를 동시에 전달



```python
# 예제) 제품별, 판매처별(김치별) 수량 판매금액 총합 평균
kimchi.groupby(by=['제품','판매처'])['수량','판매금액'].agg(['sum','mean'])
```

               수량                       판매금액              
               sum          mean          sum          mean
제품   판매처                                                   
무김치  대형마트  1550027  32292.229167  14243851204  2.967469e+08
     백화점    510114  10627.375000   5675796839  1.182458e+08
     편의점     82623   1721.312500    117134302  2.440298e+06
열무김치 대형마트  1491864  31080.500000  14272706507  2.973481e+08
     백화점    567129  11815.187500   5897836502  1.228716e+08
     편의점     89006   1854.291667    125133810  2.606954e+06
총각김치 대형마트  1649486  34364.291667  16512153282  3.440032e+08
     백화점    658442  13717.541667   6639524485  1.383234e+08
     편의점    103725   2160.937500    149010519  3.104386e+06



```python
# 예제) 제품별, 판매처별(김치별) 수량은 총합, 판매금액 평균만 >> dict() 사용
kimchi.groupby(by=['제품','판매처'])['수량','판매금액'].agg({'수량':'sum','판매금액':'mean'})
```

​            수량          판매금액

제품   판매처                        
무김치  대형마트  1550027  2.967469e+08
     백화점    510114  1.182458e+08
     편의점     82623  2.440298e+06
열무김치 대형마트  1491864  2.973481e+08
     백화점    567129  1.228716e+08
     편의점     89006  2.606954e+06
총각김치 대형마트  1649486  3.440032e+08
     백화점    658442  1.383234e+08
     편의점    103725  3.104386e+06



```python
# 멀티 레벨(agg)을 갖는 경우의 groupby 연산
kimchi_2
# 제품    판매처 
# 무김치   대형마트    1550027
#       백화점      510114
#       편의점       82623
# 열무김치  대형마트    1491864
#       백화점      567129
#       편의점       89006
# 총각김치  대형마트    1649486
#       백화점      658442
#       편의점      103725
# Name: 수량, dtype: int64
type(kimchi_2) #  pandas.core.frame.DataFrame
kimchi_2.groupby(level=0).sum()  # 제품별 총합
kimchi_2.groupby(level='제품').sum()  
kimchi_2.groupby(level=1).sum()  # 판매처별
```

