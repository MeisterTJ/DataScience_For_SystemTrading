# 단순 이동 평균 (Simple Moving Average)
# 일반적인 평균을 구하는 방법
# (n1 + n2 + n3) / 3

# 가중 이동 평균 (Weighted Moving Average)
# (w1n1 + w2n2 + w3*n3) / (w1 + w2 + w3)

# 지수 이동 평균 (Exponential Moving Average)
# 최근에 높은 가중치를 주지만, 오래된 과거도 비록 낮은 영향력이지만 가중치를 부여하도록 고려한 방법이다.
# EMV(t) = (1-w) * ((1-w) * EMV(t-2) + w * Price(t-1)) + w * Price(t)

# 골든크로스, 데드크로스는 기술적 지표인 이동평균선을 이용한 지표들이다.
# 이동평균법은 단기 추세가 장기 추세를 상향 돌파하면 매수, 하향돌파하면 매도를 한다.

# 추세가 있다면, 통계적인 관점에서 자기 상관관계가 존재할 가능성이 높다.
# 자기 상관관계가 높으면 추세를 형성할 가능성이 더 높게 된다.
# 즉, 기초자산이 random보다 자기상관 관계가 높을 때, 상승 추세 하락 추세가 더 강하게 나타난다.
# 그렇기 때문에 이동평균법을 적용할 때는 기초자산의 수익률의 자기 상관관계를 살펴서 투자 자산을 선별하면 보다 높은 성공확률을 얻을 수 있다.

import pandas as pd

def fnMA(m_Df, m_N1, m_N2, m_ColumnName='Close'):
    if m_ColumnName in m_Df.columns:
        MA1= pd.Series(pd.rolling_mean(m_Df[m_ColumnName], m_N1), name = 'MA1')
        m_Df = m_Df.join(MA1)
        MA2= pd.Series(pd.rolling_mean(m_Df[m_ColumnName], m_N2), name = 'MA2')
        m_Df = m_Df.join(MA2)

        m_Df['SignalMA']  =m_Df['MA1'] - m_Df['MA2']
        m_Df['RunMA'] = fnRun(m_Df['SignalMA'])
    else:
        raise("You didn't input a Column Name")
    return m_Df