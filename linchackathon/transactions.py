# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:50:58 2021

@author: yasse
"""

# =============================================================================
#  Imports
# =============================================================================
import requests
from . import ipaddr as u

# =============================================================================
# Buy security
# =============================================================================


def buySecurity(symbol, amount):
    """
    This function buys a security for current price

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
            amount: Number of shares

    """
    try:
        int(amount)
    except:
        raise ValueError("""The amount and price must be integers""")

    order_type = "buy"
    amount = int(amount)

    url_s = u.url + \
        f'/order?type={order_type}&symbol={symbol}&amount={amount}'

    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.post(url_s, json=body)

    return post.content.decode("utf-8")

# =============================================================================
# Sell security
# =============================================================================


def sellSecurity(symbol, amount):
    """
    This function sells a security for current price

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
            amount: Number of shares

    """
    try:
        int(amount)
    except:
        raise ValueError("""The amount and price must be integers""")

    order_type = "sell"
    amount = int(amount)

    url_s = u.url + \
        f'/order?type={order_type}&symbol={symbol}&amount={amount}'

    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.post(url_s, json=body)

    return post.content.decode("utf-8")


# =============================================================================
# Place Buy order
# =============================================================================


def placeBuyOrder(symbol, amount, price, days_to_cancel=30):
    """
    This function places an order to buy a specific stock with a specific amount
    of shares when the price of that stock goes below a certain price. Or buys instantly
    if price requested is higher than current stock price 

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
            Amount: number of shares
            price : The price for which you want the stock to be under
                    in order to buy
            days_to_cancel : How many days you want this trade to stay active:
                e.g entering 30 means that trade will be held for 30 days and then cancelled if stock price never reaches given price to buy.

        Example:
            The AAPL price currently is at 160 per share and we place an order
            so :
                placeBuyOrder('AAPL', 2, 150)

            then this order will wait until the price of the AAPL hits 150 and 
            then buys 2 shares.

            If the AAPL price is currently at 100 and we place the same order
            then it will be executed instantly and buy 2 shares for 100. Unless
            its a weekend of course then it will wait till the market is open.
    """

    try:
        int(amount)
        int(price)
        int(days_to_cancel)
    except:
        raise ValueError("""The amount and price must be integers""")

    order_type = "buy"
    amount = int(amount)
    price = int(price)
    days_to_cancel = int(days_to_cancel)

    url_s = u.url + \
        f'/order?type={order_type}&symbol={symbol}&amount={amount}&price={price}'
    if days_to_cancel is not None:
        url_s += f'&cancel_date={days_to_cancel}'

    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.post(url_s, json=body)

    return post.content.decode("utf-8")


# =============================================================================
# Place Sell order
# =============================================================================


def placeSellOrder(symbol, amount, price, days_to_cancel=30):
    """
    This function places an order to sell a specific stock with a specific amount
    of shares when the price of that stock goes below a certain price. Or buys instantly
    if price requested is higher than current stock price 

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
            Amount: number of shares
            price : The price for which you want the stock to be under
                    in order to buy
            days_to_cancel : How many days you want this trade to stay active:
                e.g entering 30 means that trade will be held for 30 days and then cancelled if stock price never reaches given price to buy.

        Example:
            The AAPL price currently is at 160 per share and we place a sell order
            so :
                placeSellOrder('AAPL', 2, 180)

            then this order will wait until the price of the AAPL hits 180 and 
            then sell 2 shares.

            If the AAPL price is currently at 200 and we place the same order
            then it will be executed instantly and sell 2 shares for 180. Unless
            its a weekend of course then it will wait till the market is open.
    """

    try:
        int(amount)
        int(price)
        int(days_to_cancel)
    except:
        raise ValueError("""The amount and price must be integers""")

    order_type = "sell"
    amount = int(amount)
    price = int(price)
    days_to_cancel = int(days_to_cancel)

    url_s = u.url + \
        f'/order?type={order_type}&symbol={symbol}&amount={amount}&price={price}'
    if days_to_cancel is not None:
        url_s += f'&cancel_date={days_to_cancel}'

    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.post(url_s, json=body)

    return post.content.decode("utf-8")

# =============================================================================
# Place Stoploss order
# =============================================================================


def placeStoplossOrder(symbol, amount, price):  # TODO: fix documentation
    """
    This function places an order to sell a specific stock with a specific amount
    of shares when the price of that stock goes below a certain price. Or buys instantly
    if price requested is higher than current stock price 

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
            Amount: number of shares
            price : The price for which you want the stock to be under
                    in order to buy
            days_to_cancel : How many days you want this trade to stay active:
                e.g entering 30 means that trade will be held for 30 days and then cancelled if stock price never reaches given price to buy.

        Example:
            The AAPL price currently is at 160 per share and we place a sell order
            so :
                placeSellOrder('AAPL', 2, 180)

            then this order will wait until the price of the AAPL hits 180 and 
            then sell 2 shares.

            If the AAPL price is currently at 200 and we place the same order
            then it will be executed instantly and sell 2 shares for 180. Unless
            its a weekend of course then it will wait till the market is open.
    """

    try:
        int(amount)
        int(price)
        int(days_to_cancel)
    except:
        raise ValueError("""The amount and price must be integers""")

    order_type = "stoploss"
    amount = int(amount)
    price = int(price)
    days_to_cancel = int(days_to_cancel)

    url_s = u.url + \
        f'/order?type={order_type}&symbol={symbol}&amount={amount}&price={price}'
    if days_to_cancel is not None:
        url_s += f'&cancel_date={days_to_cancel}'

    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.post(url_s, json=body)

    return post.content.decode("utf-8")


# =============================================================================
# cancel Order
# =============================================================================

def cancelOrder(symbol):  # TODO: fix documentation
    """
    This function is used to cancel an order on a specific stock that is still 
    active. 

        Args:
            symbol: A ticker symbol or stock symbol (ex: AAPL for Apple)
    """

    url_s = u.url + f'/cancel?order_id={symbol}'
    body = {'api_key': u.token}
    with requests.Session() as session:
        post = session.delete(url_s, json=body)

    return post.content.decode("utf-8")
