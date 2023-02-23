#!/usr/bin/env python

"""
Tests for `linchackathon` package.

BE SURE TO add api key to self.group_token from database in order to test the functions.

Tests are very simple to ensure that basic functionality is in place.
"""
# Add the parent directory of your project to your Python path
import linchackathon as lh
from linchackathon import ipaddr as u
import unittest
import pandas as pd


class TestLinchackathon(unittest.TestCase):
    def setUp(self):
        self.group_token = '438411b1-6eb8-4e1e-8c6a-0762a4beac5e'
        u.token = self.group_token
        self.expected_tickers = ['STOCK1', 'STOCK2', 'STOCK3', 'STOCK4',
                                 'STOCK5', 'STOCK6', 'STOCK7', 'STOCK8', 'STOCK9', 'STOCK10']
        self.expected_tickers_length = len(self.expected_tickers)

    def test_init_success(self):
        lh.init(self.group_token)

    def test_init_invalid_input(self):
        with self.assertRaises(ValueError):
            lh.init(12345)

    def test_getTickers(self):

        returned_tickers = lh.getTickers()
        self.assertEqual(self.expected_tickers.sort(), returned_tickers.sort())

    def test_getSecurityPrices(self):

        returned_prices = lh.getSecurityPrices()
        returned_length = len(returned_prices)

        self.assertEqual(self.expected_tickers_length, returned_length)

    def test_getHistoricSymbols(self):

        returned_historic_prices = lh.getStockHistory()
        df = pd.DataFrame(returned_historic_prices)
        print(df.head())
        self.assertGreater(len(returned_historic_prices), 0)

    def test_getHistoricSymbols_faultyTicker(self):
        with self.assertRaises(ValueError):
            lh.getStockHistory(123)

    def test_getHistoricSymbols_faultyDaysBack(self):
        with self.assertRaises(ValueError):
            lh.getStockHistory(daysback=-2)

    def test_getHistoricSymbols_nonExistantTicker(self):
        with self.assertRaises(NameError):
            lh.getStockHistory("nonexistantstonk")
