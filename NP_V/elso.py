import utils as u
import pandas as pd
import os
import matplotlib.pyplot as plt

def check_etf_price():
    etf = 'VOO'
    df = u.read_etf_file(etf)
    df[['Close', 'Adj Close']].plot()
    plt.show()
check_etf_price()

def test_return_calculation():
    u.get_etf_returns('VOO')
test_return_calculation()