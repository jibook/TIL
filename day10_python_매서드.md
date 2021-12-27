## #map #lambda #pandas #Series, DataFrame

- 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

```python
l1=['abc','def']
l2=['a/b/c','d/e/f']

l1.upper()  # list 불가
l2.split()  # list 불가

list(map(lambda x: x.upper(),l1))      #['ABC', 'DEF']
list(map(lambda x: x.split('/'),l2))   #[['a', 'b', 'c'], ['d', 'e', 'f']]
```

- pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
- Series, DataFrame 



### from pandas import Series, DataFrame

1. split

```python
l1  # ['abc', 'def']

Series(l1)
# 0    abc
# 1    def
# dtype: object

s1=Series(l1)

l2  # ['a/b/c', 'd/e/f']
Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object
s2=Series(l2)

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object
```



2. 대소치환

```python
s1
s1.str.upper()
s1.str.lower()
s1.str.title()
```

다 잘댐



3. replace

```python
s1.str.replace('a', 'A')
# 0    Abc
# 1    def
# dtype: object

s1.str.replace('a', '')
# 0     bc
# 1    def
# dtype: object
```

```python
# 예제 - 천단위 구분기호 처리
s3=Series(['1,200','3,000','4,000'])
ss3=s3.str.replace(',', '')
sum(list(map(lambda x : int(x), ss3)))
```

천단위 구분기호 때문에 문자로 인식하고 있음, 

그래서 구분기호를 없애주고

문자로 인식된것을 숫자로 바꿔주고 더해부럿지

정답 : 8200



4. 패턴 확인 : strartswith(시작하는 원소 추출), endswith(끝나는 원소 추출), conrains(포함하는 원소 추출)

```python
s1
# 0    abc
# 1    def
# dtype: object

s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool

s1[s1.str.startswith('a')]  #s1 각 원소에서 'a'로 시작하는 원소 추출
# 0    abc
# dtype: object
s1[s1.str.endswith('c')]   #s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')]   #s1 각 원소에서 'e'를 포함하는 원소 추출
```

 

5. **find (위치값 return)**

```python
# 이메일 아이디 추출
# 방법 1
s4=Series(['drwill@naver.com','zzuyu@drwill.kr'])
ss4=s4.str.find('@')
ss4
list(map(lambda x,y: x[:y],s4,ss4))

# 방법 2(잘한코드)
s4.map(lambda x : x[:x.find('@')])
```

['drwill', 'zzuyu']



6. pad : 문자열 삽입

s1.str.pad(5,             #총 자리수
                   'Left',       #삽입 방향
         		  '!')            #삽입 글자

```python
s1.str.pad(5,'left','!')
# 0    !!abc
# 1    !!def
# dtype: object

s1.str.pad(5, 'right', '?')
# 0    abc??
# 1    def??
# dtype: object

s5=Series(['i love u','you know'])
# 0    i love u
# 1    you know
# dtype: object
```


7. 문자 결합

```python
s6=Series(['abc','def','123'])
s6.str.cat()   # 'abcdef123'
s6.str.cat(sep=(','))  #'abc,def,123'
s6.str.cat(sep=('/'))  #'abc/def/123'
```

```python
s7=Series([['a','b','c'],['d','e','f']])
s7
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

s7.str.join(sep='')       #Series 내 각 원소 내부의 문자열을 결합(공백)
# 0    abc
# 1    def
# dtype: object

s7.str.join(sep=',')       #Series 내 각 원소 내부의 문자열을 결합(,)
# 0    a,b,c
# 1    d,e,f
# dtype: object
```



8. index인강

```python
s8 = Series(['a','b','c'],index=['d','e','f'])
s8 = Series(['a','b','c'],['d','e','f'])
s8
# d    a
# e    b
# f    c
# dtype: object

Series(['a','b','c'],index = ['drwill','zzuyu','hyory'])
Series(['a','b','c'],['drwill','zzuyu','hyory'])
Series(['a','b','c'],['x','y','z'])
```

