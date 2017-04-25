from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


# unittest code in Test-Driven Development with Python
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()  # 원문에는 Firefox()를 사용했으나 여기서는 Chrome()을 사용했습니다.
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:5000')  # Django 기본 포트 8000, Flask 기본 포트 5000
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '작업 아이템 입력')
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        self.fail("Finish the test!")

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

import pytest


# pytest code
class TestNewVisitor(object):

    def test_show_title(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get('http://localhost:5000')
        assert 'To-Do' in browser.title

        header_text = browser.find_element_by_tag_name('h1').text
        assert 'To-Do' in header_text

        inputbox = browser.find_element_by_id('id_new_item')
        assert inputbox.get_attribute('placeholder') == '작업 아이템 입력'

        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        inputbox = browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        table = browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  # list [<selenium.webdriver.remote.webelement.WebElement()>,]

        assert any(row.text == '1: 공작깃털 사기' for row in rows)
        assert any(row.text == '2: 공작깃털을 이용해서 그물 만들기' for row in rows)

        assert 0, "Finish the test!"
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')