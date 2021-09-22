import pandas as pd
# 가장 기본적인 새로운 행과 열을 삽입하는 방법

data = [[-4, -3, -2, -1], [1, 2, 3, 4]]
data2 = [5, 6, 7, 8]
data3 = [9, 10, 11, 12]

# list 이용하기
data_list = []
data_list.append(data)
print(data_list)    # [[[-4, -3, -2, -1], [1, 2, 3, 4]]]

data_list.append(data2)
print(data_list)    # [[[-4, -3, -2, -1], [1, 2, 3, 4]], [5, 6, 7, 8]]

data_list.insert(0, data3)
print(data_list)    # [[9, 10, 11, 12], [[-4, -3, -2, -1], [1, 2, 3, 4]], [5, 6, 7, 8]]

# ### pandas 새로운 row 추가하기
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
print(df)               # ABCD를 열로 하고,  data를 row로 하는 DataFrame 생성
#    A  B  C  D
# 0 -4 -3 -2 -1
# 1  1  2  3  4

temp_df = pd.DataFrame([data2], columns=['A', 'B', 'C', 'D'])
# df 아래에 temp_df를 붙인다.
df = pd.concat([df, temp_df]).reset_index(drop=True)
print(df)
#    A  B  C  D
# 0 -4 -3 -2 -1
# 1  1  2  3  4
# 2  5  6  7  8

# A, B, C, D 를 col로 하고 각 위치에 data3의 값들을 열로 하는 DataFrame을 생성한다.
temp_df = pd.DataFrame({"A": data3[0], "B": data3[1], 'C': data3[2], 'D': data3[3]}, index=[0])
df = pd.concat([temp_df, df]).reset_index(drop=True)
print(df)
#    A   B   C   D
# 0  9  10  11  12
# 1 -4  -3  -2  -1
# 2  1   2   3   4
# 3  5   6   7   8

# ### pandas 새로운 column 추가하기
sz = len(df)    # row의 갯수
data2 = [i * 100 for i in range(sz)]

# 열 이름이 colAdd 이고, [0, 100, 200, 300] 을 각 행으로 갖는 시리즈를 생성
temp = pd.Series(data2, name='colAdd')

# DataFrame 맨 오른쪽에 Series를 붙인다.
df = df.join(temp)
print(df)
#    A   B   C   D  colAdd
# 0  9  10  11  12       0
# 1 -4  -3  -2  -1     100
# 2  1   2   3   4     200
# 3  5   6   7   8     300