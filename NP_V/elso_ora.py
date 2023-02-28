import pandas as pd
import numpy as np

df_iei = pd.read_csv('IEI.csv', index_col=0)
df_voo = pd.read_csv('VOO.csv', index_col=0)

df_iei = df_iei[['Adj Close']]
df_iei = df_iei.rename(columns={'Adj Close': 'Adj Close_iei'})
df_voo = df_voo[['Adj Close']]
df_voo = df_voo.rename(columns={'Adj Close': 'Adj Close_voo'})

df_merge = df_iei.join(df_voo, how='inner')



pass