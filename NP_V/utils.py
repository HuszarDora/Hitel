import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


def read_etf_file(etf):
    filename = os.path.join(etf + '.csv')
    df = pd.read_csv(filename, index_col=0)
    df.index = pd.to_datetime(df.index)
    return df

# def check_etf_price():
#     etf = 'VOO'
#     df = read_etf_file(etf)
#     df[['Close', 'Adj Close']].plot()
#     plt.show()
# check_etf_price()


def get_etf_returns(etf_name, return_type='log', fieldname='Adj Close'):
    df = read_etf_file(etf_name)
    df = df[[fieldname]]
    df['shifted']=df.shift(1)
    if return_type == 'log':
        df['return'] = np.log(df[fieldname]/df['shifted'])
    if return_type == 'simple':
        df['return'] = (df[fieldname]/df['shifted'])-1
    return df[['return']]


df_voo_return = get_etf_returns('VOO')
df_iei_return = get_etf_returns('IEI')



def get_total_returns_a(etf, return_type='log'):
    df = get_etf_returns(etf, return_type, 'Adj Close')
    return df


def get_dividend_return(etf, return_type='log'):
    # calc total simple return from Adj Close and Close
    df_ret_from_adj = get_etf_returns(etf, 'simple', 'Adj Close')
    df_ret_from_close = get_etf_returns(etf, 'simple', 'Close')

    # simple div= ret Adj Close - ret Close simple
    df_div = df_ret_from_adj-df_ret_from_close

    # convert log if log
    if return_type == 'log':
        df_div = np.log(df_div+1)
    return df_div

def test_plot_divident_return():
    df = get_dividend_return('VOO', 'simple')
    df.plot()
    plt.show()
test_plot_divident_return()



def get_price_return(etf, return_type='log'):

    pass




pass