# =============================================================================
#  Imports
# =============================================================================
import requests
from . import ipaddr as u

# =============================================================================
# Get orders
# =============================================================================


def get_orders():
    """
    This function returns a list of all the order that you have placed
    (completed and active)
    """

    return get_completed_orders() + get_pending_orders()

# =============================================================================
# Get completed orders
# =============================================================================


def get_completed_orders():
    """
    This function returns a list of all the order that are completed
    """

    url_g = u.url + '/account/get_completed_orders'
    body = {"api_key": u.token}
    with requests.Session() as session:
        get = session.get(url_g, json=body)

    return get.json()


# =============================================================================
# Get pending orders
# =============================================================================

def get_pending_orders():
    """
    This function returns a list of all the order that are completed
    """

    url_g = u.url + '/account/open_orders'
    body = {"api_key": u.token}
    with requests.Session() as session:
        get = session.get(url_g, json=body)

    return get.json()


# =============================================================================
# Get stoploss orders
# =============================================================================

def get_stoploss_orders():
    """
    This function returns a list of all the order that are completed
    """

    url_g = u.url + '/account/get_stoploss_orders'
    body = {"api_key": u.token}
    with requests.Session() as session:
        get = session.get(url_g, json=body)

    return get.json()


# =============================================================================
# get saldo
# =============================================================================

def get_saldo():
    """
    This function returns an integer representing your current balance
    """

    url_g = u.url + f'/account/saldo'
    body = {"api_key": u.token}
    response = requests.get(url_g, json=body)

    return response.json()


# =============================================================================
# get portfolio
# =============================================================================

def get_portfolio():
    """
    This function returns a dictionary that contains the amount of shares you 
    own from each stock.
    """

    url_g = u.url + '/account/portfolio'
    body = {"api_key": u.token}
    response = requests.get(url_g, json=body)

    return response.json()
