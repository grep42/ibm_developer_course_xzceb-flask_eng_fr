import unittest
from unittest.mock import patch
import sys
import os


# Add the parent directory of 'Tests' to sys.path
tests_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(tests_dir)
sys.path.insert(0, parent_dir)


# Now import the required functions
from translator import english_to_french, french_to_english, run_prompts




class TestTranslator(unittest.TestCase):




    @patch('builtins.input', return_value='')
    def test_null_input_english_to_french(self, mock_input):
        # Test that the function returns None when passed a null input for english_to_french
        result = english_to_french()
        self.assertIsNone(result)




    @patch('builtins.input', return_value='')
    def test_null_input_french_to_english(self, mock_input):
        # Test that the function returns None when passed a null input for french_to_english
        result = french_to_english()
        self.assertIsNone(result)




    def test_hello_to_bonjour(self):
        # Test that the function translates 'Hello' to 'Bonjour' for english_to_french
        english_text = 'Hello'
        expected_french_text = 'Bonjour'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_french_text)




    def test_bonjour_to_hello(self):
        # Test that the function translates 'Bonjour' to 'Hello' for french_to_english
        french_text = 'Bonjour'
        expected_english_text = 'Hello'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_english_text)




if __name__ == '__main__':
    unittest.main()
