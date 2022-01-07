## Python 팁이라기보다 기초^^;



```python 
'abcadaedags'.strip('a') # 'bcadaedags' : 'a'가 양끝에 있을 경우만 제거해줌
'abcadaedags'.replace('a','') # 'bcdedgs : 모든 'a'를 제거해줌
```



```python
vname='apeachee'
vemail='apeachee@gmail.com'
jumin='960505-2222222'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1] == 'm'  # F
vname[1] == 'p'  # T

# 2. vemail에서 이메일 아이디만 추출
vemailid=vemail.find('@')
vid=vemail[:vemailid]
vid    # 'apeachee'

# 3. 주민번호에서 여자인지 확인 (참고: 남자:1, 여자:2)
jumin.find('-')
list(jumin.split('-'))
jumin.split('-')       # ['960505', '2222222']
jumin.split('-')[0]    # '960505'   
jumin.split('-')[1]    # '2222222'   
jumin.split('-')[1][0] # '2'
```



#### for 반복문, if 조건문

**반복제어문**

1. continue : 특정 조건일 경우 반복문 스킵

2. break : 특정 조건일 경우 반복문 종료 (정지 조건)
3. exit : 특정 조건일 경우 프로그램 종료 **이런건 웬만하면 하지마 다 날려버리기 싫으면**
4. pass : 문법적으로 오류가 발생시키지 않기 위해 자리를 채우는 역할



```python
# 1부터 100까지 총 합
# 방법 1
vsum = 0
for i in range(1,101):
    vsum = vsum + i
print(vsum)

# 방법 2
vvv = sum(i for i in range(1,101))
print(vvv)
```

5050

i          vsum                     일반화
1          1                         vsum+1
2          1+2                     vsum+2
3          1+2+3                vsum+3
4          1+2+3+4            vsum+4
                                            ----> vsum+1



```python
# 1~100까지 짝수 총합
# 대박힌트
# if i%2==1:  # 만약 i를 2로 나누어서 나온 나머지가 1이면 --> 홀수이면
# if i%2==0:  # 만약 i를 2로 나누어서 나온 나머지가 0이면 --> 짝수이면

vsuum=0
for i in range(1,101):
    if i%2==0:
        vsuum+=i  
print(vsuum)
```

2550



```python
# 다음의 리스트 선언하고 5보다 클 경우 'A', 작거나 같을 경우 'B'
l1=[1,3,5,15,25]
for i in l1:
    if i > 5:
        print('A')
    else:
        print('B')
```

B
B
B
A
A



```python
#1부터 100까지 누적합이 최초 2000 이상이 되는 시점의 k값과 총합을 출렷하세요
# 1+2+3+...+k>=2000
k=0
for i in range(1,101):
    k=k+i
    if k>=2000:
       break
print(i,k)
```

63 2016



#### while

```python
# while 문으로 1부터 10까지 출력
i = 1
while i <= 10:
    print(i)
    i = i+1
```

1

2

3

4

5

6

7

8

9

10

#### append() 

append()는 새로운 요소를 array 맨 끝에 객체로 추가함.

```python
nums = [1,2,3]
nums.append(4)
# [1,2,3,4]

nums.append([5,6])
# [1,2,3,4,[5,6]]
```

리스트를 추가하려 했지만, 추가되지 않고 `'[5'` 와 `'6]'`형태로  추가된 것을 볼 수 있음.

```python
# l1 리스트에 각 원소에 10을 더해서 출력
l1=[1,3,5,15,25]
l2=[]
for i in l1:
    l2.append(l1+10)
print(l2)
```

[11, 13, 15, 25, 35]



### def

def 함수이름(인수1, 인수2, 인수3):

​		함수 본문

​		return 반환할 객체 

```python
# 숫자를 넣어서 곱하기 10한 값을 반환
def f_mul(x):
    v1=x*10
    return v1

f_mul(100)
```

1000



```python
# 두 숫자(두개의 인자를 넣는구낭) 넣어서 두 숫자의 곱을 변환
def f_2_mul(x,y):
    v1=x*y
    return v1
print(f_2_mul(2,10))

# or
def f_2_mul(x,y):
    return (x*y)
print(f_2_mul(2,10))
```

20



```python
def f_d (y,x=1):
    return(x*y)
# default 값을 갖는 인수를 맨 뒤에 배치

def f_d (x=1,y=1):
    return(x*y)
print(f_d())
```

1



#### lambda 축약형

비교적 단순한 연산 및 리턴시 사용

```python
# 예제 1,
f1= lambda x: x*10
f1(10) 

# 예제 2, 3개 숫자를 전달받아 첫 번째와 두번째 합에 세번째 숫자의 곱 리턴
f2= lambda x,y,z: (x+y)*z
f2(3,4,5)
```

예제 1: 100

예제 2: 35



```python
# 예제 3,
f1= lambda x: x*10
f1(4)

# 예제 4,
l1[1,2,4,10]
f1(l1)
```

예제 3 : 40

예제 4: [1,
 3,
 5,
 15,
 25,
 1,
 3,

...

ㅋㅋ리스트가 열번 반복



### map 함수

사용자 정의 함수 + map 함수

map(func,           #적용할 함수

​          iterable)    #추가할 인수

```python
f1=lambda x: x*10
f1(4)
# 40

map(f1,l1)
# <map at 0x257c14082e0>

l1[1,2,4,10]
list(map(f1,l1))
# [10, 20, 40, 100]
```



```python
# 하나의 숫자를 전달받을거에요 10보다 크면 3을 곱하고, 작거나 같으면 2를 곱한 결과를 리턴하세요
l2=[3,5,7,12]

def f3(x):
    if x >10:
        v3= x*3
    else:
        v3= x*2
    return v3

f3(11)  # 33
f3(5)   # 10
f3(l1)  # list는 에러

list(map(f3, l2))
# [6, 10, 14, 36]
```





복습은 미리미리 밀리지 않게 합시다,,