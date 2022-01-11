# NA 결측치 처리, 중복값 제거, 전처리 왕중요!

### 1. NA 수정

```python
s1.mean()       # NaN 값 제외하고 평균값 산출함 >> 2.0
s1.fillna(0)    # fillna 사용한 치환 >> 제일 많이 활용함
''' NaN에 0으로 치환, 숫자로 인식
0    1.0
1    2.0
2    3.0
3    0.0
dtype: float64
'''
s1.replace(np.nan,'a')   # replace 활용, 값 치환 메소드 NA 치환 가능
''' 오브젝트로 인식 1도 str 1로 인식
0    1.0
1    2.0
2    3.0
3      a
dtype: object
'''
```

- 조건 색인을 해서 NA 처리 가능 

```python
s1.isnull()           # bool(T/F) 값으로 도출
s1[s1.isnull()]=0     # 조건 색인을 해서 처리
'''
0    1.0
1    2.0
2    3.0
3    0.0
dtype: float64
'''
```



### 2. NA 로의 수정

```python
s3=Series(['서울','.','대전','.','대구','.','부산'])
s3.replace('.',np.nan)
'''
0     서울
1    NaN
2     대전
3    NaN
4     대구
5    NaN
6     부산
dtype: object
'''
```

