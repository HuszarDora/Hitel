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



def get_total_return(etf, return_type='log'):
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
# test_plot_divident_return()

def test_plot_total_return():
    df = get_total_return('VOO', 'log')
    df.plot()
    plt.show()
# test_plot_total_return()



def get_price_return(etf, return_type='log'):
    df_total = get_total_return(etf, 'simple')
    df_div = get_dividend_return(etf, 'simple')
    df_price = df_total - df_div
    if return_type == 'log':
        df_price = np.log(df_price+1)
    return df_price

def get_portfolio_return(d_pf, return_type='log'):
    # join returns
    # drop na
    # multiply by weights
    # sum across etfs
    # give back rsult


    df_result = pd.DataFrame
    for etf, weight in d_pf.items():
        if df_result is None:
            df_result = weight * get_total_return(etf, 'simple')
        else:

        df_result = df_result.add(df_result, df_ret)
    return df_result

def test_portfolio_return():
    d_pf={'VOO':0.6, 'IEI':0.4}
    get_portfolio_return(d_pf, 'simple')
test_portfolio_return()


pass