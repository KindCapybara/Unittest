from unittest import TestCase
from ya_api import create_folder, get_folder_info

folder_name = 'test_folder'


class TestYaAPI(TestCase):

    def test_create_folder(self):
        result = create_folder(folder_name)
        self.assertTrue(result, 201)

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(folder_name), 'dir')
