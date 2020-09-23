import unittest

from classes.validator import validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_if_too_long(self):
        # assume
        username = 'InvalidTooLong'

        # action
        result = self.validator.username_is_valid(username)

        # assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_white_space_present(self):
        # assume
        username = 'White Space'

        # action
        result = self.validator.username_is_valid(username)

        # assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_no_uppercase_characters(self):
        # assume
        username = 'lowercase'

        # action
        result = self.validator.username_is_valid(username)

        # assert
        self.assertFalse(result)

    def test_it_will_accept_valid_username(self):
        # assume
        username = 'Valid'

        # action
        result = self.validator.username_is_valid(username)

        # assert
        self.assertTrue(result)
