# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:08:56 2021

@author: yasse
"""


# =============================================================================
#  Imports
# =============================================================================
from typing import List
import requests
import pandas as pd
import numpy as np
from . import ipaddr as u

# =============================================================================
# Getting all the tickers
# =============================================================================


def get_tickers() -> List[str]:
    """
    This function returns a list with all the tickers.

    """

    ticker_url = u.url+'/symbols'
    response = requests.get(ticker_url)
    response_json = response.json()

    return response_json


# =============================================================================
# Getting One point data One ticker
# =============================================================================

# TODO: remove this? Instead use getSecurity price and locate ticker from that dataframe
def get_stock(ticker) -> dict:
    """
    This function takes in one argument, which is the ticker, as a string 
    and returns the current price of the stock.

        Args:
            ticker : the ticker symbol or stock symbol (ex: AAPL for Apple)

    """
    if type(ticker) != str:
        raise ValueError("The ticker must be a string")

    gstock_url = u.url + '/public/' + ticker
    response = requests.get(gstock_url)

    return response.json()


# =============================================================================
# Getting One point data One ticker
# =============================================================================


def get_security_prices() -> pd.DataFrame:
    """
    This function return the current prices of all stocks in a dataframe

        Args:
            ticker : the ticker symbol or stock symbol (ex: AAPL for Apple)

    """

    try:
        gstock_url = u.url + '/data/stocks'
        response = requests.get(gstock_url)
    except Exception as e:
        print(f"errror: {str(e)}")

    response_json = response.json()
    df = pd.DataFrame(response_json['data'])
    return df


# =============================================================================
# Getting Multiple point data One ticker
# =============================================================================

def get_security_history(days_back: int, ticker: str = None) -> dict:
    """
    This function utilizes the getStock function and returns the history. It 
    requires the ticker and the ammount of days in the past. You can also
    insert 'all' in the ticker argument to get the history of all the stocks
    instead of a specifc one.

        Args:
            ticker : the ticker symbol or stock symbol (ex: AAPL for Apple)
            daysback : an integer specifying the number of days to scrape from
                       in the past

    """
    if days_back < 0 or days_back > 365:
        raise ValueError("""
        You have entered a negative value for days back, it must be psotive.
        """)
    if ticker is not None and ticker not in u.tickers:
        raise NameError("""

                The Ticker you included is incorrect.
                Check the Tickers available by running 'getTickers()'
                
                """)
    params = {'days_back': days_back}
    if ticker:
        params['ticker'] = ticker
    body = {"api_key": u.token}
    response = requests.get(u.url + '/data', params=params, json=body)

    return response.json()
