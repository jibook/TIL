## 알고리즘

- 정렬 : 선택정렬
  - 종류는 많지만 결국 **오름차순**으로 결과의 형태가 다를 뿐, 같은 방식으로 처리됨
- 검색 : 순차 검색, 이진 검색(*)
  - 이진 검색 : 꼭 정리가 되어있어야함.
- 재귀 : 정복하슛!



### 1. 정렬

- 종류는 많지만 결국 **오름차순**으로 결과의 형태가 다를 뿐, 같은 방식으로 처리됨

```python
## 함수
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if(ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 전역
testAry = [55, 88, 33, 77]

## 메인
minPos = findMinIndex(testAry)
print('제일 작을 값-->', testAry[minPos])
```



- 선택 정렬 1

```python
import random
## 선택정렬 1 (가장 쉬운 정렬이지만, 실제로 써도 됨)
## 함수
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if(ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 전역
before = [ random.randint(1,99) for _ in range(20) ]
after = []

## 메인
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)
```



- 선택 정렬 2

```py
import random
## 선택정렬 2
## 함수
def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) : # 0, 1, 2 (제일 작은값)
        minIdx = i
        for k in range(i+1, n) :
            if (ary[minIdx] > ary [k]) :
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return  ary

## 전역
dataAry = [ random.randint(1,99) for _ in range(20) ]

## 메인
print('정렬전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬후 -->', dataAry)

```



### 2. 검색 

- 이진 검색 : 꼭 정리가 되어있어야함.
 


- 순차검색

```python
import random
## 순차 검색
## 함수
def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)
    for i in range(size) :
        if ary[i] == fData :
            pos = i
            break
    return pos

## 전역
dataAry = [ random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0,len(dataAry)-1)]

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
    print(findData, ' 없습니다.');
else :
    print(findData, ':', position, ' 위치에 있음')
```



- 이진 검색 : 핵중요

```python
import random
## 이진 검색(=탐색)
## 함수
def binarySearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary) - 1
    while (start <= end) :
        mid = (start + end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return pos
## 전역
dataAry = [ random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0,len(dataAry)-1)]
dataAry.sort()


## 메인
print('배열-->', dataAry)
position = binarySearch(dataAry, findData)
if position == -1 :
    print(findData, ' 없습니다.');
else :
    print(findData, ':', position, ' 위치에 있음')
```





### 3. 재귀 호출(Recursion)

- 재귀 호출 : 자신을 다시 호출하는 것



```python

## 재귀 1
## 함수 선언부
def openBox() :
    print('상자열기')
    openBox()
    
    
## 메인 코드 
openBox()


## 재귀 2
## 함수 선언부
def openBox() :
    global count
    print('상자열기')
    count -= 1
    if count == 0 :
        print('##반지넣기##')
        return
    openBox()
    print('상자닫기')
    return
    
    
## 메인 코드 
count = 5
openBox()



## 재귀 3
## 함수 선언부

# 10부터 1까지 합계 구하기
def addNumber(num) :
    if num <= 1 :
        return 1
    return num + addNumber(num-1)
print(addNumber(10))

# 10! 구하기
factValue = 1
for n in range(10, 0, -1) :
    factValue *= n
print("10*9*8*..*1", factValue)



# 카운트 다운
def countDown(n) :
    if n == 0 :
        print('발사!')
    else :
        print(n)
        countDown(n-1)
        
countDown(5)
    

# 별모양 출력하기
def printStar(n) :
    if n > 0 :
        printStar(n-1)
        print('별'*n)
        
printStar(5)
        

# 구구단 출력하기
def gugu(dan, num) :
    print("%d x %d = %d" % (dan, num, dan*num))
    if num < 9 :
        gugu(dan, num+1)
        
for dan in range(2,10) :
    print("## %d단 ##" % dan)
    gugu(dan,1)


# n제곱 계산하기
tab=''
def pow(x, n) :
    global tab
    tab += ''
    if n == 0 :
        return 1
    print(tab + "%d*%d^(%d-%d)" % (x, x, n, 1))
    return x * pow(x, n-1)

print('2^4')
print('답-->', pow(2,4))


# 배열의 합 계산하기
import random

def arySum(arr, n) :
    if n <= 0 :
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]


print(ary)
print('배열 합계 ->', arySum(ary, len(ary)-1))


```

