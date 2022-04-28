## Algorithm 

#### 자료구조

1. 선형 : 한줄로 서기

   - 선형 리스트 : 따다닥 붙어있기, (배열)공간절약, 접근빠름. 삽입/ 삭제에서 오버헤드 발생

   - (단순) 연결 리스트 : 논리적으로는 선형과 동일. 물리적으로 떨어져있음. 삽입/ 삭제에서 오버해드 X

     ​          						접근이 느림. 용량이 많이.

   - 원형 연결 리스트 : 처음과 끝이 이어진 것

   - 스택(*) : 한쪽 끝이 막힌 구조. FILO(first in last out,= LIFO)

     ​				push, pop, top (탑이 -1이면 비어있다.)

   - 큐

     - 일반큐 : 오버해드 발생, front = rear = -1
     - 원형큐 : 오버해드 X, front = rear = 0, 1칸을 사용 못함, rear + 1 == front, % SIZE

2. 비선형 : 여러줄로 서기
   - 트리 : 나무를 거꾸로 뒤집어 놓은 형태 
     - 이진 탐색 트리 
   - 그래프 : 개념, 연관 행렬





--------------------------------------



#### 큐(Queue)

- 입구와 출구가 따로 있는 원통 형태
- 인큐(enQueue) : 큐에 데이터를 삽입하는 작동
- 데큐(deQueue) : 데이터를 추출하는 작동
- 프론트(front) : 저장된 데이터 중 첫번째 데이터
- 리어(rear) : 저정된 데이터 중 마지막 데이터

프론트와 리어가 같으면 비어있다.



1. 데이터 삽입 인큐(enQueue)

리어를 하나 늘리고 그자리에 입력



#### 이진 트리

- 이진 트리 노드 구성 : 오른쪽 링크 + 데이터 + 왼쪽 링크

```python
## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
## 전역
memory=[]
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :  # ['레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if (current.data > name) :
            if (current.left == None) :
                current.left = node
                break
            current = current.left
        else :
            if (current.right == None):
                current.right = node
                break
            current = current.right
    memory.append(node)

print('이진 탐색 트리 구성 완료!')
```



```python
## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
## 전역
memory=[]
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :  # ['레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if (current.data > name) :
            if (current.left == None) :
                current.left = node
                break
            current = current.left
        else :
            if (current.right == None):
                current.right = node
                break
            current = current.right
    memory.append(node)

print('이진 탐색 트리 구성 완료!')

findName = '마마부'

current = root
while True :
    if current.data == findName :
        print(findName, '찾았음. 야호~~~')
        break
    elif current.data > findName :
        if current.left == None :
            print(findName, '이 트리에 없어요ㅠ')
            break
        current = current.left
    else :
        if current.right == None :
            print(findName, '이 트리에 없어요ㅠ')
            break
        current = current.right


```





#### 그래프

- 무방향 그래프 : 간선에 방향성이 없는 그래프 
- 가중치 그래프 : 
- 깊이 우선 탐색의 작동 

```python
## 함수
class Graph() :
    def __init__(self, size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

## 전역
G = None

## 메인
G = Graph(4)

G.graph[0][1] = 1; G.graph[0][2] = 1; G.graph[0][3] = 1
G.graph[1][0] = 1; G.graph[1][2] = 1
G.graph[2][0] = 1; G.graph[2][1] = 1; G.graph[2][3] = 1
G.graph[3][0] = 1; G.graph[3][2] = 1


print("## 무방향 그래프##")
for row in range(4) :
    for col in range(4) :
        print(G.graph[row][col], end = ' ')
    print()
```



-------------------------

#### 알고리즘

- 정렬 : 선택정렬
  - 종류는 많지만 결국 **오름차순**으로 결과의 형태가 다를 뿐, 같은 방식으로 처리됨
- 검색 : 순차 검색, 이진 검색(*)
  - 이진 검색 : 꼭 정리가 되어있어야함.
- 재귀 : 정복하슛!



##### 정렬

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

