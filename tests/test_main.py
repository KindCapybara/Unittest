from main import *
from unittest import TestCase


class TestVisit(TestCase):

    def test_matching(self):
        result = search_visit_ru()
        self.assertIsInstance(result, list)

    def test_count_visit(self):
        res = search_visit_ru()
        self.assertEqual(len(res), 6)

    def test_search_visit(self):
        for visits in search_visit_ru():
            for visit, [sity, country] in visits.items():
                self.assertIn('Россия', country)


class TestId(TestCase):

    def test_matching(self):
        result = search_uniq_id()
        self.assertIsInstance(result, list)

    def test_unique_elements(self):
        result = search_uniq_id()
        set_result = list(set(result))
        self.assertEqual(result, set_result)


class TestMaxSalesAmount(TestCase):

    def test_amount(self):
        result = max_sales_amount()
        self.assertEqual(len(result), 2)
