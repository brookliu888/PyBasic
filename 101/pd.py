import pandas as pd
import matplotlib

'''
s = pd.Series([1, 2, 3, 4])
print(s)

date = pd.date_range("20201101", periods=30)
print(date)
s = pd.Series(range(1, 31), index=date)
print(s)
print(s.loc["20201118"])
print(s.loc["20201118":"20201130"])
print(s.iloc[15:20])
'''
l = [1,2,3,4,5,6]
date_index = pd.date_range("20201101", periods=6)
s = pd.Series(l,index=date_index)
print(s)
print(s.max())
print(s.std())
print(s.min())
print(s.cumsum())
print(s.cumprod())
s.plot()