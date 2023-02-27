import requests
from . import ipaddr as ip_address


def get_all_orders():
    """
    Returns a list of all completed and pending orders
    """
    return get_completed_orders() + get_pending_orders()


def get_completed_orders():
    """
    Returns a list of completed orders
    """
    url = ip_address.url + '/account/get_completed_orders'
    body = {"api_key": ip_address.token}
    with requests.Session() as session:
        response = session.get(url, json=body)
    return response.json()


def get_pending_orders():
    """
    Returns a list of pending orders
    """
    url = ip_address.url + '/account/open_orders'
    body = {"api_key": ip_address.token}
    with requests.Session() as session:
        response = session.get(url, json=body)
    return response.json()


def get_stoploss_orders():
    """
    Returns a list of stoploss orders
    """
    url = ip_address.url + '/account/get_stoploss_orders'
    body = {"api_key": ip_address.token}
    with requests.Session() as session:
        response = session.get(url, json=body)
    return response.json()


def get_balance():
    """
    Returns an integer representing the current balance
    """
    url = ip_address.url + f'/account/saldo'
    body = {"api_key": ip_address.token}
    response = requests.get(url, json=body)
    return response.json()


def get_portfolio():
    """
    Returns a dictionary with the amount of shares owned for each stock
    """
    url = ip_address.url + '/account/portfolio'
    body = {"api_key": ip_address.token}
    response = requests.get(url, json=body)
    return response.json()
