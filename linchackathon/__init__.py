# -*- coding: utf-8 -*-

"""
LINC
======

This package is required in order to participate in the LINC Hackathon (Lund University Finance Society). 


"""

from .auth import init
from .historic_symbols import getTickers, getStock, getStockHistory, getSecurityPrices
from .transactions import placeBuyOrder, placeSellOrder, placeStoplossOrder, buySecurity, sellSecurity
from .account import getOrders, getCompletedOrders, getPendingOrders, getSaldo, getPortfolio
from .stoploss import placeStoploss, deleteStoploss, getStoplosses
