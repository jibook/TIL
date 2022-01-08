## stack, unstack, pivot_table

- 자료구조(datatype) 형태
- long type(tidy data) : 각 속성을 컬럼으로 표현 
- wide data(cross table : 교차표) : 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열함



1. stack : wide ->> long
2. unstack : long --> wide

```python
df2=df1.unstack()    # long --> wide 행이 컬럼이 바뀐다 대각선을 기준으로 
df2.stack()   
```

