# 스토캐스틱은, 최근 N일간의 최고가와 최저가의 범위 내에서 현재 가격의 위치를 표시할 때,
# 매수세가 매도세보다 강할 때는 그 위치가 높게 형성되고, 매도세가 매수세보다 강할 때는 그 위치가 낮게 형성된다는 것을 이용한 것이다.

# 기술적 지표중에서 사용빈도가 높고 신뢰성이 높은 모멘텀 지표이다.
# %K : n기간 동안 고가 저가 범위 중 금일 종가가 어디에 위치해 있는지를 알려주는 지표
# %D(Slow %K) : %K의 3일 동안의 이동평균값
# Slow %D : %D의 3일 동안 이동평균값

# %K = 100[(C - L)/(H - L)] (일반적으로 n은 14가 많이 이용됨)
# 100% 라면 현재 가격이 N일간 최고가이므로 매수세가 가장 강한 경우
# 0%라면 현재 가격이 N일간 최저가이므로 매도세가 가장 강한 경우가 된다.

# C = 최근 종가
# L = 기간 n 중에 가장 작은 값
# H = 기간 n 중에 가장 큰 값
# %D = K의 단순이동평균값(SMA, 일반적으로 3일 이용)

# 과매도 구간에서(75이상) Slow %K선이 Slow %D를 상향 돌파하면 매수
# 과매수 구간에서(25이하) Slow %K선이 Slow %D를 하향 돌파하면 매도

import pandas as pd


def fnStoch(df, n=14):  # price: 종가(시간 오름차순), n: 기간
    df_size = len(df['Close'])

    if df_size < n:
        # show error message
        raise SystemExit('입력값이 기간보다 작음')

    tempSto_K = []

    for i in range(df_size):
        if i >= n - 1:
            tempUp = df['Close'][i] - min(df['Low'][i - n + 1:i + 1])
            tempDown = max(df['High'][i - n + 1:i + 1]) - min(df['Low'][i - n + 1:i + 1])
            tempSto_K.append(tempUp / tempDown)
        else:
            tempSto_K.append(0)  # n보다 작은 초기값은 0 설정
    df['Sto_K'] = pd.Series(tempSto_K, index=df.index)

    df['Sto_D'] = pd.Series(pd.rolling_mean(df['Sto_K'], 3))
    df['Sto_SlowD'] = pd.Series(pd.rolling_mean(df['Sto_D'], 3))

    return df
