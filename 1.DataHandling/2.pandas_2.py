import pandas as pd
import numpy as np

# pandas를 이용할 때 정렬하고, index를 갱신하는 방법에 대해서 배워본다.

data1 = [12000, 11590, 13110, 14000]
data2 = [20151015, 20151015, 20151014, 20151014]
data3 = [1000, 901, 902, 1400]

data = [data1, data2, data3]
# data:  [[12000, 11590, 13110, 14000], [20151015, 20151015, 20151014, 20151014], [1000, 901, 902, 1400]]
print('data: ', data)

# 전치 행렬 함수 (2차원 리스트를 행렬로 만든다.)
# numpy.ndarray
newData = np.transpose(data)
# transposed data:
#  [[   12000 20151015     1000]
#  [   11590 20151015      901]
#  [   13110 20151014      902]
#  [   14000 20151014     1400]]
print('transposed data: \n', newData)

# columns 아래로 전치 행렬을 집어 넣은 DataFrame을 생성한다.
df = pd.DataFrame(newData, columns=['Close', 'Date', 'Time'])
# dataframe:
#     Close      Date  Time
# 0  12000  20151015  1000
# 1  11590  20151015   901
# 2  13110  20151014   902
# 3  14000  20151014  1400
print('DataFrame: \n', df)

# Date, Time 순으로 오름 차순으로 정렬한다. (Date가 같을 경우 Time으로 결정)
df = df.sort_values(['Date', 'Time'], ascending=[True, True])
# sorted data:
#     Close      Date  Time
# 2  13110  20151014   902
# 3  14000  20151014  1400
# 1  11590  20151015   901
# 0  12000  20151015  1000
print('sorted data: \n', df)

# 인덱스를 재갱신한다.
df = df.reset_index(drop=True)
# reindexed data:
#     Close      Date  Time
# 0  13110  20151014   902
# 1  14000  20151014  1400
# 2  11590  20151015   901
# 3  12000  20151015  1000
print('re indexed data: \n', df)
