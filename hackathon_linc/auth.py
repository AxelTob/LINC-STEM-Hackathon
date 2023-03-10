# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:08:56 2021

@author: yasse
"""

# =============================================================================
#  Imports
# =============================================================================
import requests
from . import ipaddr as u
from .historic_symbols import get_all_tickers

# =============================================================================
# Initialize
# =============================================================================


def init(group_token: str):
    """
    Initializes the connection and authenticates the token.

    Args:
        group_token (str): The token for authentication.

    Raises:
        ValueError: If the token is not a string.

        NameError: If the token is not valid.

    Returns:
        None: Prints a welcome message.
    """

    if type(group_token) == str:
        pass
    else:
        raise ValueError("""
                               
            You have entered a wrong value. Make sure that the token is in the 
            form of a string like : 
                    
                    '171beb3a-b3bc-4j76-9s89-39332218106e' """)

    u.token = group_token

    u.tickers = u.tickers + get_all_tickers()

    url = u.url

    auth_url = url + '/auth/login'
    body = {"api_key": u.token}
    response = requests.post(auth_url, json=body).status_code

    if response == 200:
        pass
    else:
        raise NameError("""
                              
            The token you entered is not valid. Please make sure that its spelled
            correctly and try again. Contact someone for support if you get this 
            more than once. 
            
            """)

    print(f"""

    Welcome to the LINC Hackathon! Your token is now saved in the Console. 
    That means you don't need to carry that out when using the other functions
    as long as you don't close your console. 
    
    This function is only to be used once to authenticate your token.

    You can use the link below to view the dashboard:

    hackathon.linclund.com
    
    Happy coding!

    """)
