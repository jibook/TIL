# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:53:57 2021

@author: jhjh3
"""

### python_3_조건문과 반복문

# 논리 연산자
# and
# or
# not

v1 = 1
(v1>=3 and (v1<=7))
(v1>=3 % (v1<=7))

v11 = 5
(v11>=3 and (v11<=7))
(v11>=3 % (v11<=7))

(v1>=3 or (v1<=7))    # True
(v1>=3 | (v1<=7))     # False

not(v1==1)            # False

#조건문 if 

#형식
# if 조건 : 
#      참(True)일 때 실행 문장
# else:
#     거짓(False)일 때 실행 문장

# if 조건1 : 
#    조건1이 참(True)일 때 실행 문장
# else 조건2:
#    조건1이 거짓(False)이면서 조건2가 참일 때 실행 문장
# else:
#    조건1,2가 모두 거짓(False)일 때 실행 문장

v1 = 4

if v1>5:
    print('A')
else:
    print('B')   #'B'
    
# 리스트는 불가     
l1=[1,2,3,4,5]    
if l1>5:
    print('A') 
else:
    print('B')
# TypeError: '>' not supported between instances of 'list' and 'int'
    

# 반복문
# 객체의 각 원소에 동일한 연산처리 진행할 경우 사용
# 1. for 문 : 정해진 횟수, 대상이 있을 경우 

# for 반복변수 in 반복할 대상(범위):
#     반복 실행할 문장

#1~10까지 출력하시오.
range(1,11)

for i in range (1,11):
    print(i)

# 예제 
# 다음의 리스트 선언하고 5보다 클 경우 'A', 작거나 같을 경우 'B'

l1=[1,3,5,15,25]
for i in l1:
    if i > 5:
        print('A')
    else:
        print('B')

# 위 리스트에서 각 원소에 10을 더해서 출력
l1+10    #불가

for i in l1:
    print(i+10)

# for 문의 결과를 바로 변수로 저장하는 건 불가
l1 = for i in l1:
       print(i+10)

# 정답
l2=[]
for i in l1:
    l2.append(i+10)
print(l2)
# [11, 13, 15, 25, 35]

nums = [1,2,3]
nums.append(4)
nums
nums.append([5,6])
nums

l3=[1,2,3]
l3.append(4)
l3

# while 문 : 조건에 따른 반복을 실행하는 경우
# while 조건 :
#    조건이 참일 때 반복 문장
    
# 예제
# while 문으로 1~10까지 출력

i=1
while i <=10:
    print(i)
    i = i+1

# 문제
# 1~100까지 총 합
vsum=0
for i in range(1,101):
    vsum = vsum + i
print(vsum)

vsum=0
for i in range(1,11):
    vsum = vsum +i
print(vsum)

vvv = sum(i for i in range(1,101))
print(vvv)

# 1~100까지 짝수 총합
# 대박힌트
# if i%2==1:  # 만약 i를 2로 나누어서 나온 나머지가 1이면 --> 홀수이면
# if i%2==0:  # 만약 i를 2로 나누어서 나온 나머지가 0이면 --> 짝수이면

vsuum=0
for i in range(1,101):
    if i%2==0:
        vsuum+=i
        
print(vsuum)

vsum=0
for i in range(1,101):
    if i%2==0:
        vsum+=i
        
print(vsum)

#반복제어문
#1. continue : 특정 조건일 경우 반복문 스킵
#2. break : 특정 조건일 경우 반복문 종료 (정지 조건)
#3. exit : 특정 조건일 경우 프로그램 종료
#4. pass : 문법적으로 오류가 발생시키지 않기 위해 자리를 채우는 역할

#예제 
# 1~10 출력, 5제외
for i in range(1,11):
    if i ==5:
        continue
    print(i)

# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

v1 = 1
if v1 > 10:
    pass
else:
    print('b')
# b

#문제
#1부터 100까지 누적합이 최초 2000 이상이 되는 시점의 k값과 총합을 출렷하세요
# 1+2+3+...+k>=2000

k=0
for i in range(1,101):
    k=k+i
    if k >= 2000:
        print(i)
        break
print(k)


vk=0
for i in range(1,101):
    vk=vk+i
    if vk>=2000:
        break
print(i,vk)



### python_4_사용자 정의함수

# 사용자 정의 함수
# 사용자가 정의하는 함수의 형태
# input과 output 관계를 내부에 정의 
# def, lambda(축약형)

# 함수 정의 
# f(x)=x+1

# 1. def 방식

# def 함수이름(인수1, 인수2, 인수3):
#     함수 본문
#     return 반환할 객체 

# 숫자르 넣어서 곱하기 10한 값을 반환

def f_mul(x):
    v1=x*10
    return v1

f_mul(100)

# 두 숫자(두개의 인자를 넣는구낭) 넣어서 두 숫자의 곱을 변환

def f_2_mul(x,y):
    v1=x*y
    return v1
print(f_2_mul(2,10))

def f_2_mul(x,y):
    return (x*y)
print(f_2_mul(2,10))

# 20



#lambda 축약형
#비교적 단순한 연산 및 리턴시 사용

#예제 : 숫자를 넣을거예요, 여기에 10을 곱한 값을 리턴하세요

f1= lambda x: x*10
f1(10)

#문제
#3개 숫자를 전달받아 첫 번째와 두번째 합에 세번째 숫자의 곱 리턴
f2= lambda x,y,z: (x+y)*z
f2(3,4,5)


f1= lambda x: x*10
f1(4)

l1= [1,2,4,10]
f1(l1)

# for 문 처리
l2=[]
for i in l1:
    l2.append(i+10)
print(l2)

# [11, 13, 15, 25, 35]


# 사용자 정의 함수 + map 함수
# map(func,        #적용할 함수
#     iterable)    #추가할 인수

#f1=lambda x: x*10
f1(4)
map(f1,l1)
# <map at 0x257c14082e0>
list(map(f1,l1))
[10, 30, 50, 150, 250]

#하나의 숫자를 전달받을거에요 10보다 크면 3을 곱하고, 작거나 같으면 2를 곱한 결과를
#리턴하세요

l2=[3,5,7,12]

def f3(x):
    if x >10:
        v3= x*3
    else:
        v3= x*2
    return v3

f3(11)
f3(5)
f3(l1) # list는 에러
list(map(f3, l2))
# [6, 10, 14, 36]



