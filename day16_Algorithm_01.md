## Algorithm 개념

1. **자료구조**

- 선형 자료구조 : 한 줄로 순차적으로 표현된 형태 
  - 리스트(List) (=!파이썬 리스트 : 배열Array) : 선형, 원형 연결, 원형 연결
  - 스택(*)
  - 큐 : 일반 큐, 원형 큐

- 비선형 자료구조 
  - 트리 : 이진탐색 트리
  - 그래프 : 범위가 많음, 연관 행렬



2. **알고리즘** : 어떤 문제를 해결해 가는 논리적인 과정

 - 알고리즘 성능 측정 : 시간 복잡도(Time Complexity)
 - 빅-오 표기법(Big-Oh Notation) : O(f(n)) 형태
   - O(1) : 완벽에 가까운 알고리즘, 나올 수 없다. 
   - O(log n) : 이진검색
   - O(n)
   - O(n log n) :  퀵 정렬
   - O(n**2) 
   - O(n**3)
   - O(2**n)

 - 정렬 : 선택정렬
 - 검색 : 순차 검색, 이진 검색(*)
 - 재귀 : 잘 아는 것이 중요 



### 리스트

- 선형 리스트 : 일정한 순서로 나열한 자료구조
- (단순)연결 리스트 : 논리적으로 따다닥, 물리적으로는 멀리
- 원형 연결 리스트 : 시작 위치와 마지막 위치가 연결되는 형태, 오버해드가 발생하지 않음.
- 순차 리스트(Ordered List)
- 입력 순서대로 저장하는 데이터에 적당



#### 선형 리스트

1. 데이터 만들기

```python
def add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

add_data('갑인')
add_data('병자')
add_data('경신')

print(katok)


insert_data(3,'신유')
print(katok)
```

['갑인', '병자', '경신']



2. 데이터 삽입

```python
def insert_data(position, friend) :
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) : 
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend
    
    
add_data('정사')
print(katok)
```

['갑인', '병자', '경신', '정사']



3. 데이터 삭제 

```python
def delete_data(position) : 
    katok[position] = None
    kLen = len(katok)
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])    
    
    
delete_data(3)
print(katok)    
```

['갑인', '병자', '경신']



#### 단순 연결 리스트 

- 논리적으로 따다닥, 물리적으로는 멀리
- 선형 리스트에서 데이터 삽입 : 오버헤드 발생(많은 작업)
- 단순 연결 리스트에서 데이터 삽입 : 오버헤드 발생 안함
- 노드 구조 : 데이터 + 링크 로 구성된 항목
- 헤드(노드) > 노드 > 노드 > 노드



1. 노드(데이터) 삽입

​	새노드 생성 > 링크 수정 

```python
## 함수/클래스 선언부
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current , pre
    if head.data == findData : # 첫 노드 앞에 삽입할 때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 사나 앞에 솔라를 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막에 추가할 때 (=삽입할 이름이 존재하지 않으때)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return


## 전역 변수
memory = [  ]
head, current , pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
node = Node() # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :   # ['정연', '쯔위', '사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNode(head)
```





2. 노드(데이터) 삭제

```python
def deleteNode(deleteData) :
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data :
        current = head
        head = head.link
        del(current)
        return
    # 첫 노드 외의 노드 삭제
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

node2.link = node3.link
del(node3)

deleteNode('쯔위')
printNode(head)
deleteNode('재남')
printNode(head)
```



3. 중간 노드를 찾을 떄

```python
def findNode(findData) :
    global memory, head, current, pre
    current = head
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node()


fNode = findNode('다현')
print(fNode.data)
fNode = findNode('사나')
print(fNode.data)
fNode = findNode('재남')
print(fNode.data)
```



4. 연결해보면,,

```python
## 함수/클래스 선언부
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current , pre
    if head.data == findData : # 첫 노드 앞에 삽입할 때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 사나 앞에 솔라를 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막에 추가할 때 (=삽입할 이름이 존재하지 않으때)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return


def deleteNode(deleteData) :
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data :
        current = head
        head = head.link
        del(current)
        return
    # 첫 노드 외의 노드 삭제
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

def findNode(findData) :
    global memory, head, current, pre
    current = head
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node()

## 전역 변수
memory = [  ]
head, current , pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
node = Node() # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :   # ['정연', '쯔위', '사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNode(head)

insertNode('다현', '화사')
printNode(head)
insertNode('사나', '솔라')
printNode(head)

deleteNode('화사')
printNode(head)
deleteNode('쯔위')
printNode(head)

fNode = findNode('다현')
print(fNode.data)
fNode = findNode('사나')
print(fNode.data)
```





#### 스택(Stack)

- 스택 자료구조는 한쪽 끝이 막힌 형태
- 입구가 하나이기 때문에 먼저들어간 것이 가장 나중에 나오는 구조(선입후출, 후입선출)
- 탑가지고 조절



```python
## 함수
def  isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return  True
    else :
        return  False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False


## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
stack = ['커피', '녹차', '꿀물', '콜라', None]
top=3

push('맥주')
print(stack)
push('포도주')
print(stack)

```



```python
## 함수
def  isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return  True
    else :
        return  False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅~')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
stack = ['커피', None, None, None, None]
top=0

print(pop())
print(pop())
```





알고리즘  정렬, 검색, 재귀

재귀 정복해라,,





