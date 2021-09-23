# MACD (Moving Average Convergence / Divergence)
# MACD = EMA(numFast) - EMA(numSlow)
# numFast, numSlow 기간으로 MACD값을 산출하고 이를 c기간의 EMA를 시그널 선으로 활용한다.
# 일반적으로 MACD(12, 26, 9)가 많이 사용된다.
def fnMACD(m_Df, m_NumFast=12, m_NumSlow=26, m_NumSignal=9):
    m_Df['EMAFast'] = m_Df['price'].ewm(span=m_NumFast, min_periods=m_NumFast - 1).mean()
    m_Df['EMASlow'] = m_Df['price'].ewm(span=m_NumSlow, min_periods=m_NumSlow - 1).mean()
    m_Df['MACD'] = m_Df['EMAFast'] - m_Df['EMASlow']
    m_Df['MACDSignal'] = m_Df['MACD'].ewm(span=m_NumSignal, min_periods=m_NumSignal - 1).mean()
    m_Df['MACDDiff'] = m_Df['MACD'] - m_Df['MACDSignal']
    return m_Df
