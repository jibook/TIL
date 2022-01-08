## np.arange()

```python
np.arange(10,61,19).reshape(2,3)   
```

- 10부터 60까지 10간격으로, 2줄 3컬럼



## merge vs. concat

- 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기  
- 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
- 참조 조건 사용, 연관된 두 데이터를 병합(join)

```python
pd.merge(left,             # 첫번째 데이터프레임
         right,            # 두번째 데이터프레임
         how='inner',      # 조인 방법(default = 'inner' ), 기본값
         on=,              # 조인하는 컬럼(컬럼명이 서로 같을 때) 
         left_on=,         # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
         right_on=)        # 두번째 데이터프레임 조인(컬럼명이 서로 다를 때)
```





## concat()

```python
pd.concat([df1,df2])
# 행의 결합 >> 기본은 세로방향으로 합쳐짐
pd.concat([df1,df2], axis=0)
pd.concat([df1,df2], ignore_index=True) # 순차적인 인덱스 번호 부여됨
#    A   B   C
# 0   1   2   3
# 1   4   5   6
# 0  10  20  30
# 1  40  50  60

pd.concat([df1,df2], axis=1) # 가로방향으로 합쳐짐 (열의 방향)
#    A  B  C   A   B   C
# 0  1  2  3  10  20  30
# 1  4  5  6  40  50  60
```





## merge()

```python
pd.merge(left,             # 첫번째 데이터프레임
         right,            # 두번째 데이터프레임
         how='inner',      # 조인 방법(default = 'inner' ), 기본값
         on=,              # 조인하는 컬럼(컬럼명이 서로 같을 때) 
         left_on=,         # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
         right_on=)        # 두번째 데이터프레임 조인(컬럼명이 서로 다를 때)
```



```python
pd.merge(emp, df_dept, on='deptno' )
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000    인사부
# 1      2  allen      10  4500    인사부
# 2      4  grace      10  4200    인사부
# 3      3   ford      20  4300    총무부
# 4      6   king      20  4000    총무부
# 5      5  scott      30  4100  IT분석부
```

- inner가 디폴트값이고 dname으로 정렬된 것을 확인할 수 있음



#### outer join

```python
pd.merge(emp, df_dept_new, on='deptno') # 30번 부서원 생략
   empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀

pd.merge(emp, df_dept_new, on='deptno', how='outer')
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀
# 5      5  scott      30  4100    NaN
```



## drop()

- 특정 행, 컬럼 제거

- 이름 전달



```python
emp.loc[emp['ename']=='scott']   # scott 관련된 record
#   empno  ename  deptno   sal
# 4      5  scott      30  4100
emp.loc[emp['ename']=='scott',:]       # 스캇만 보여줘
emp.loc[~(emp['ename']=='scott'),:]  # 스캇빼고 보여줘 ~

#### scott 빼기
emp.drop(4, axis=0)     # 행기준, 4번째 idx 제외
```



## shift

- 행 또는 열을 이동

- 전일자 대비 증감율

```python
emp['sal']  # dtype: int64 정수
emp['sal'].shift()  #default : aixs=0 (행), dtype : float64 실수
```



#### 예제) 다음 데이터프레임에서 전일자 대비 증감율 출력

```python
s1
# 2021/01/01    3000
# 2021/01/02    3500
# 2021/01/03    4200
# 2021/01/04    2800
# 2021/01/05    3600
# dtype: int64

s1.shift()
# 2021/01/01       NaN
# 2021/01/02    3000.0
# 2021/01/03    3500.0
# 2021/01/04    4200.0
# 2021/01/05    2800.0
# dtype: float64
```

- 1월 2일 증감률 >> (3500-3000)/3000

```python
(s1-s1.shift())/s1.shift()*100
# 2021/01/01          NaN
# 2021/01/02    16.666667
# 2021/01/03    20.000000
# 2021/01/04   -33.333333
# 2021/01/05    28.571429
# dtype: float64
```



## rename()

- 행, 컬럼명 변경 

```python
emp.columns = ['emptno','ename','deptno','salary']

emp.rename({'salary':'sal','deptno':'dept_no'}, axis=1)   # 컬럼대로 바꿔줌 
```



#### 예제) emp 데이터에서 ename을 idx로 설정 후 scott 을 SCOTT 변경

```python
emp
emp.set_index('ename')   # ename을 맨앞, 즉 인덱스로 설정
#        emptno  deptno  salary
# ename                        
# smith       1      10    4000
# allen       2      10    4500
# ford        3      20    4300
# grace       4      10    4200
# scott       5      30    4100
# king        6      20    4000


# 1.
emp_1 = emp.set_index('ename')
emp_1.rename({'scott':'SCOTT'},axis=0)

# 2.
emp.set_index('ename').rename({'scott':'SCOTT'})

# 3.
emp.index = emp['ename']
emp.rename({'scott':'SCOTT'}, axis = 0)
```



- 데이터명.set_index('떙떙')    # '땡떙'으로 인덱스 명이 지정되는거야
