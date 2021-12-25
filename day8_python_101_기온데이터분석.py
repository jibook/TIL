## 모두의 데이터 분석 with 파이썬
#열공하슈


import csv

f = open('C:/Users/jhjh3/Desktop/jicode/data/seoul_copy.csv', 'r', encoding='utf-8') #cp949
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
# print(data)
for row in data:
    print(row)
f.close()

# ['\t\t지점번호', '지점명', '일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', '평균최저기온(℃)', '최저기온(℃)', '최저기온일자']
# ['\t\t108', '서울', '2008-01', '-1.7', '1.9', '7.3', '2008-01-06', '-5.0', '-11.1', '2008-01-17']
# ['\t\t108', '서울', '2008-02', '-1.2', '3.2', '10.5', '2008-02-22', '-4.9', '-10.1', '2008-02-13']
# ...


f = open('C:/Users/jhjh3/Desktop/jicode/data/seoul_copy.csv', 'r', encoding='utf-8') #cp949
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
# print(data)
# for row in data:
#     print(row)
f.close()

# 헤더(header) : 데이터 파일에서 여러가지 값들이 어떤 의미를 갖는지 표시한 행을 나타낸다. 
#                쉽게 말해 밑 예시로 쩌것들, 근데 왜 밑에 항목까지 다나왓을꼬ㅋㅋ
# ['\t\t지점번호', '지점명', '일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', '평균최저기온(℃)', '최저기온(℃)', '최저기온일자']



# 1. 데이터에서 최고 기온을 실수로 변환, 한행 씩 출력
f = open('C:/Users/jhjh3/Desktop/jicode/data/seoul_copy.csv', 'r', encoding='utf-8') #cp949
data = csv.reader(f, delimiter=',')
header = next(data)
# print(header)
for row in data:
    row[5] = float(row[5]) # 최고 기온을 실수로 변환
    print(row)

f.close() 

# 실수로 변환하는 이유는 'str'문자로 알고 있기 때문에 float 실수, 즉 숫자로 인식하게 하기 위함이다.
# 딱히 변한게 없어보이지만 컴퓨터한테는 큰 변화가 있었을 것이다.

# ['\t\t지점번호', '지점명', '일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '\t최고기온일자', '평균최저기온(℃)', '최저기온(℃)', '최저기온일자']
# ['\t\t108', '서울', '2008-01', '-1.7', '1.9', '7.3', '2008-01-06', '-5.0', '-11.1', '2008-01-17']
# ['\t\t108', '서울', '2008-02', '-1.2', '3.2', '10.5', '2008-02-22', '-4.9', '-10.1', '2008-02-13']
# ['\t\t108', '서울', '2008-03', '7.3', '11.9', '19.8', '2008-03-21', '3.7', '-1.7', '2008-03-05']
# ...


# 2. 최고 기온과 최고 기온이었던 날짜를 찾으세요.
f = open('C:/Users/jhjh3/Desktop/jicode/data/seoul_copy.csv', 'r', encoding='utf-8') #cp949
data = csv.reader(f, delimiter=',')
header = next(data)

# 최고기온, 해당하는 날짜

# 초기화 (여기에 일단 예시를 넣어주고 여기 값을 원하는 값으로 바꿀 변수를 만든겨)
max_temp = -999
max_date = ''

# print(header)

for row in data:
    if row[5] == '' :
    # 1. 누락된 데이터 처리, 빈 문자열을 -999로 표시하는 느낌 
        row[5] = -999
    row[5] = float(row[5])  # 문자를 실수형 변경
    # 2. 비교해서 최고 기온 찾아서, 최고기온과 해당되는 일자를 찾앗
    if max_temp < row[5]:  # 만약 빈칸 즉 -999보다 높은 기온이다 그러면
        max_temp = row[5]  # max_temp에 넣엇
        max_date = row[6]  # max_temp에 해당하는 날짜를 넣엇
    # print(row)

f.close()

print(max_temp,max_date)
print('2008년도 이후 서울 최고 기온이 가장 높았던 날은',max_date,'이고',max_temp,'도 였습니다')

# 39.6 2018-08-01
# 2008년도 이후 서울 최고 기온이 가장 높았던 날은 2018-08-01 이고 39.6 도 였습니다


# 촤란

