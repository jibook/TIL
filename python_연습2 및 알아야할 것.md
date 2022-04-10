#### DataFrame

DataFrame(np.arange(1,7).reshape(2,3), index=['a','b'], columns=['col1','col2','col3'])
```   A  B  C
a  1  2  3
b  4  5  6
```

np.arange(1,7).reshape(2,3)

```array([[1, 2, 3],
array([1,2,3],[4, 5, 6])
```


#### iloc, loc ****

- iloc : positional indexing 숫자로 위치를 뽑아옴[행인덱스,열인덱스]
- loc(location) : label indexing 해당하는 행을 뽑아온다



#### 예제 - 이메일 아이디 추출 / 맵람다형태확인

s6=Series(['abc@abc.com','avcvdds@abc.com'])

1. s6.map(lambda x: x[:x.find('@')])
2. s6.map(lambda x: x[:x.find('@')])
3. list(s6.map(lambda x: x[:x.find('@')]))
4. s6id=s6.str.find('@')
   list(map(lambda x,y: x[0:y],s6,s6id))



#### 문자열 제거(제거함수 : 공백, 문자)

Series(map(lambda x: x.replace('a',''),['aaabaaca','abcba']))
Series(['aaabaaca','abcba']).str.replace('a','')

Series(['abcd','abcde','aaaab']).str.replace('a', 'A')



#### [예제] 천단위 구분기호 처리

s3=Series(['1,200','3,000','4,000'])
s3.str.replace(',','')

``` 0    1200
1    3000
2    4000
dtype: object
0    1200
1    3000
2    4000
dtype: object
```

s3.str.replace(',','').astype(int)              # 객체에서 숫자로 바꿔줘야 합할 수 있지
s3.str.replace(',','').astype(int).sum()   # 더했다! 8200



#### df1.sum(axis=0)    열
#### df1.sum(axis=1)    행





#### [예제] df1에 천단위 구분기호 제거 후 모두 숫자 변경

df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])

edf1= lambda x : x.find(',')

list(map())

df1.DataFrame(find(','))    




df1.applymap(lambda x : int(x.replace(',',''))).sum()



##### 동료 코드1

```python
copy_df1=df1
for i in range(0,len(df1)):
    copy_df1[i]=df1[i].str.replace(',','')
print(copy_df1)

#      0     1
#0  1200  1300
#1  1400  1500
```

  0     1

0  1200  1300
1  1400  1500

##### 동료 코드2

```python
df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
for i in range(len(df1)):
    if df1[i].all() != 'int':
        df1[i] = df1[i].str.replace(',','').astype('int')
    else:
        pass
print(df1)

#      0     1
#0  1200  1300
#1  1400  1500
```



#### '.' 확인 시 NaN으로 변경

```
import numpy as np

df1['a'][df1['a'] == '.'] = np.nan  # 점발견
```

3    .

Name: a, dtype: object



#### train/test 로 나눠서 데이터 분석(머신러닝에선 필쑤!!)

- 학습전에 스케일링을 시키고 해야함

train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)
