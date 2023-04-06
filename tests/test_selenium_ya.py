from unittest import TestCase
from selenium_ya import selenium_login, correct_login


class TestYandexAuth(TestCase):
    def test_login(self):
        self.assertTrue(correct_login())

    def test_auth(self):
        result = selenium_login()
        self.assertTrue(result, "https://id.yandex.ru/")
