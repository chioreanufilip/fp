# from laborator_5.ui import *
# # import unittest
# # from unittest.mock import patch
#
# # class Teste:
# #     @patch('build')
# # def test_suchen():
# #     assert suchen_der_name_addresse() ==5
# import unittest
# from unittest.mock import patch, MagicMock
# # from your_module import suchen_customer_function
#
# class TestSuchenCustomerFunction(unittest.TestCase):
#
#     @patch('builtins.input', side_effect=['TestClient'])
#     @patch('your_module.Controller')
#     def test_suchen_customer_function_found(self, mock_controller, mock_input):
#         # Set up the mock results for filter_by_adress and filter_by_name
#         mock_controller().filter_by_adress.return_value = [MagicMock()]
#         mock_controller().filter_by_name.return_value = [MagicMock()]
#
#         # Call the function
#         suchen_der_name_addresse()
#
#         # Assertions
#         mock_controller().filter_by_adress.assert_called_once_with('TestClient')
#         mock_controller().filter_by_name.assert_called_once_with('TestClient')
#         self.assertEqual(mock_input.call_count, 1)  # Ensure input was called only once
#
#     @patch('builtins.input', side_effect=['TestClient'])
#     @patch('your_module.Controller')
#     def test_suchen_customer_function_not_found(self, mock_controller, mock_input):
#         # Set up the mock results for filter_by_adress and filter_by_name
#         mock_controller().filter_by_adress.return_value = []
#         mock_controller().filter_by_name.return_value = []
#
#         # Set up the mock result for the second input
#         mock_input.side_effect = ['2']
#
#         # Call the function
#         suchen_der_name_addresse()
#
#         # Assertions
#         mock_controller().filter_by_adress.assert_called_once_with('TestClient')
#         mock_controller().filter_by_name.assert_called_once_with('TestClient')
#         self.assertEqual(mock_input.call_count, 2)  # Ensure input was called twice
#
# if __name__ == '__main__':
#     unittest.main()
