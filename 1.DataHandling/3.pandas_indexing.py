import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(7, 2), index=range(0, 21, 3), columns=list(['A', 'B']))
print(df)
print(df.loc[6])
print(df.iloc[6])