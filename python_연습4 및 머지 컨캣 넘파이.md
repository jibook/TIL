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

