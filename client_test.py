import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771',
             'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            bid_price = float(quote['top_bid']['price'])
            ask_price = float(quote['top_ask']['price'])
            price = (bid_price + ask_price) / 2
            data_point = (quote['stock'], bid_price, ask_price, price)
            self.assertEqual(getDataPoint(quote), data_point)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771',
             'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        data_point = getDataPoint(quotes[0])
        self.assertTrue(data_point[1] > data_point[2])
        data_point = getDataPoint(quotes[1])
        self.assertFalse(data_point[1] > data_point[2])

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_is_zero(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771',
             'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        datapoint_a = getDataPoint(quotes[0])
        datapoint_b = getDataPoint(quotes[1])
        self.assertEqual(getRatio(datapoint_a[3], datapoint_b[3]), None)

    def test_getRatio_calculateRatio(self):
        quotes = [
            {'top_ask': {'price': 100, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 200, 'size': 109}, 'id': '0.109974697771',
             'stock': 'ABC'},
            {'top_ask': {'price': 150, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 100, 'size': 81}, 'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        datapoint_a = getDataPoint(quotes[0])
        datapoint_b = getDataPoint(quotes[1])
        self.assertEqual(getRatio(datapoint_a[3], datapoint_b[3]), 1.2)


if __name__ == '__main__':
    unittest.main()
