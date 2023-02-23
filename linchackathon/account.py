# =============================================================================
#  Imports
# =============================================================================
import requests
from . import ipaddr as u

# =============================================================================
# Get orders
# =============================================================================


def getOrders():
    """
    This function returns a list of all the order that you have placed
    (completed and active)
    """

    url_g = u.url + '/private/' + u.token + '/order'
    with requests.Session() as session:
        get = session.get(url_g)

    return get.json()


# =============================================================================
# Get completed orders
# =============================================================================

def getCompletedOrders():
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

def getPendingOrders():
    """
    This function returns a list of all the order that are completed
    """

    url_g = u.url + '/account/open_orders'
    body = {"api_key": u.token}
    with requests.Session() as session:
        get = session.get(url_g, json=body)

    return get.json()


# =============================================================================
# get saldo
# =============================================================================

def getSaldo():
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

def getPortfolio():
    """
    This function returns a dictionary that contains the amount of shares you 
    own from each stock.
    """

    url_g = u.url + '/account/portfolio'
    body = {"api_key": u.token}
    response = requests.get(url_g, json=body)

    return response.json()
