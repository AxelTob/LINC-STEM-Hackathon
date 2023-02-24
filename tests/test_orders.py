"""
Tests for `linchackathon` package.

BE SURE TO add api key to self.group_token from database in order to test the functions.

Tests are very simple to ensure that basic functionality is in place.
RUN test 1 by 1 to check that everything works, bit goofy but hey.
"""
# Add the parent directory of your project to your Python path
import linchackathon as lh
from linchackathon import ipaddr as u
import unittest
import time


class TestLinchackathon(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.expected_orders_completed = 0
        self.expected_orders_pending = 0

    def setUp(self):
        self.group_token = 'ccc6816e-654d-4ecd-ac20-c7aba17cb0e9'
        self.starting_saldo = 10000  # HARDCODED
        u.token = self.group_token
        self.expected_tickers = ['STOCK1', 'STOCK2', 'STOCK3', 'STOCK4',
                                 'STOCK5', 'STOCK6', 'STOCK7', 'STOCK8', 'STOCK9', 'STOCK10']
        self.expected_tickers_length = len(self.expected_tickers)

    def test_init_success(self):
        lh.init(self.group_token)

    def test_completedOrders_empty(self):
        returned_orders = lh.getCompletedOrders()
        self.assertEqual(len(returned_orders), 0)

    def test_pendingOrders_empty(self):
        returned_orders = lh.getPendingOrders()
        self.assertEqual(len(returned_orders), 0)

    def test_add_pendingOrder(self):
        symbol = "STOCK1"
        amount = 1
        price = 1  # Price we never will buy at
        result = lh.placeBuyOrder(symbol, amount, price, days_to_cancel=40000)
        if result:
            self.expected_orders_pending += 1

        pending_orders = lh.getPendingOrders()
        self.assertEqual(len(pending_orders), self.expected_orders_pending)

    def test_placeBuyOrder(self):
        symbol = "STOCK2"
        amount = 2
        price = 5000  # Price we will buy at

        result = lh.placeBuyOrder(symbol, amount, price)
        result_str = result[0:6]
        self.assertEqual(result_str, '{"amou')

    def test_placeSellOrder(self):
        symbol = "STOCK2"
        amount = 1
        price = 0  # Price we sell at

        result = lh.placeSellOrder(symbol, amount, price)
        result_str = result[0:6]
        self.assertEqual(result_str, '{"amou')

    def test_buySecurity(self):
        symbol = "STOCK8"
        amount = 1
        result = lh.buySecurity(symbol, amount)
        result_str = result[0:6]
        self.assertEqual(result_str, '{"amou')

    def test_sellSecurity(self):
        symbol = "STOCK8"
        amount = 1
        result = lh.sellSecurity(symbol, amount)
        result_str = result[0:6]
        self.assertEqual(result_str, '{"amou')

    def test_placeSellOrder_notOwned(self):
        # SELLING STOCK WE DONT OWN TEST
        symbol = "STOCK5"
        amount = 1
        price = 2  # Price we will sell at

        result = lh.placeSellOrder(symbol, amount, price)
        result_str = result[0:6]
        self.assertEqual(result_str, '(psyco')

    def test_getSaldo(self):
        result = lh.getSaldo()
        saldo = result['saldo']

        self.assertGreaterEqual(saldo, 0, msg="saldo not recieved")

    def test_getPortfolio(self):
        result = lh.getPortfolio()
        portfolio_size = len(result)
        self.assertEqual(portfolio_size, 1)

    def test_stopLoss(self):
        # TODO: Test stoplosses
        pass

    def test_cancelOrder(self):
        # TODO: test this
        pass
