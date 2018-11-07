import unittest

from order_verify import *

class TestOrder(unittest.TestCase):

    def test_order_status(self):
        order_id = 2
        self.assertEqual(check_order_status(order_id), True)

    def test_id_is_intenger(self):
        order_id = "ds"
        self.assertEqual(if_integer(order_id), False)

    def test_pending_order(self):
        order_id = 2
        self.assertFalse(not_delivered_yet(order_id))

    def test_order_doesnot_exist(self):
        order_id = 1000
        self.assertEqual(order_validation(order_id), True) 

    def test_whether_orders_added_list(self):
        pending_orders = [4, 5, 6, 8]
        delivered_orders = [1, 2, 32, 100]
        self.assertTrue(added_to_the_list())

    def test_add_new_order_to_list(self):
        order_id = 67
        self.assertEqual(add_new_order_to_list(67), "Added new order to the list")

    def test_order_delivered(self):
        order_id = 6
        self.assertEqual(order_delivered(order_id), "order delivered sucessfully")