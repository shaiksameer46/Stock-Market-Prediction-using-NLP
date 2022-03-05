# %%
import numpy as np
import pandas as pd
import pandas_datareader as pdr


# %%
def get_spy_trend(s_date, e_date):
    """ Load spy trends from Yahoo! Finance

    Parameters
    ----------
    s_date : str
        The start date of data sample
    e_date : str
        The end date of data sample

    Returns
    -------
    spy : Series
        S&P 500 trends from Yahoo! finance
    """

    spy = pdr.get_data_yahoo('SPY', s_date, e_date)
    spy = np.sign(spy['Adj Close'].diff()).shift(-1)

    return spy



