import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def read_etf_file(etf):
    filename = os.path.join(etf + '.csv')
    df = pd.read_csv(filename, index_col=0)
    df.index = pd.to_datetime(df.index)
    return df

def check_etf_price():
    etf = 'VOO'
    df = read_etf_file(etf)
    df[['Close', 'Adj Close']].plot()
    plt.show()
check_etf_price()


def get_etf_returns(etf_name, return_type='log', fieldname='Adj Close'):
    df = read_etf_file(etf_name)
    df = df[[fieldname]]
    df['shifted']=df.shift(1)
    if return_type=='log':
        df['return'] = np.log(df[fieldname]/df['shifted'])
    if return_type == 'simple':
        df['return'] = (df[fieldname]/df['shifted'])-1
    return df[['return']]

get_etf_returns()