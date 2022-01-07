## Python

```python
# ',' 문자 제거 >>> 숫자 변경 
# 천단위 구분기호 제거 >>> 컬럼 변경

'19,200'.replace(',', '')
int('19,200'.replace(',', ''))
'19,200'.replace(',', '').astype('int')
# 문자열에 사용 불가(array, Series, DataFrame 사용 가능)   

f1 = lambda x: int(x.replace(',',''))
card = card.applymap(f1)
card
```

#### applymap : 2차원 데이터셋 (DataFrame)에 통!!!!으로 함수적용 위해 사용

int('19,200'.replace(',', ''))

이 행위(형변환 함수)를 전체에 적용할 때 사용해요



```python
# 일자별 총합 (새로운 열 생성)
card['총합'] = card.sum(axis=1)
card
```

   식료품      의복    외식비      책값  온라인소액결제    의료비      총합

NUM                                                      
1    19400  143000   8600   29000     5600  19200  224800
2    22200  120400   7000   26000     3300  13000  191900