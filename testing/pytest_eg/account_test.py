import unittest
from mock import Mock, patch

from app.account import Account

class testAccount(unittest.TestCase):
    def test_get_account_returns_data_for_id_1(self):
        account_data = {"id":"1", "name":"test"}
        # we can Mock external dependencies ssuch as services, API endpoints etc.
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        # use the mock as we instantiate an Account
        account = Account(mock_data_interface)
        # now make a unittetst asertion
        # wrong = {"id":"2", "name":"test"} # this fails the test!
        # self.assertDictEqual( wrong, account.get_account(1) )
        self.assertDictEqual( account_data, account.get_account(1) ) # this passes the test
    def test_account_conn_exception(self):
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = ConnectionError()
        # mock_data_interface.wibble_list = ['wibble', 'wobble']
        account = Account(mock_data_interface)
        self.assertEqual("Connection error occurred. Try Again.", account.get_account(1) )
    # we can patch services etc.
    @patch('app.account.requests')
    def test_current_balance(self, mock_requests): # mock_the thing we patched
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'any old text'
        mock_requests.get.return_value = mock_response
        account = Account(Mock())
        self.assertEqual({'status':200, 'data':'any old text'}, account.get_current_balance('1'))

if __name__ == '__main__':
    unittest.main()