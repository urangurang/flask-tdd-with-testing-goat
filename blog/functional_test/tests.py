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
        self.check_for_row_in_list_table('1: 공작깃털 사기')
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')

        self.fail("Finish the test!")

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

import pytest


# pytest code
class TestNewVisitor(object):

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        assert any(row_text in row.text for row in rows)

    @staticmethod
    def url_match(url):
        raise ValueError(url)

    def test_show_title(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get('http://localhost:5000')
        assert 'To-Do' in self.browser.title

        header_text = self.browser.find_element_by_tag_name('h1').text
        assert 'To-Do' in header_text

        inputbox = self.browser.find_element_by_id('id_new_item')
        assert inputbox.get_attribute('placeholder') == '작업 아이템 입력'

        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url

        # excinfo == Exception Informantion
        with pytest.raises(ValueError) as excinfo:
            self.url_match(edith_list_url)

        # self.assertRegex(edith_list_url, '/lists/.+')
        assert excinfo.match(r'/lists/.+')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("1: 공작깃털 사기")
        self.check_for_row_in_list_table("2: 공작깃털을 이용해서 그물 만들기")

        page_text = self.browser.find_element_by_tag_name('body').text
        assert '공작깃털 사기' in page_text
        assert '그물 만들기' in page_text

        # 프란시스가 새로운 작업 아이템을 입력하기 시작한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)

        # 프란시스가 전용 URL을 취득
        francis_list_url = self.browser.current_url
        with pytest.raises(ValueError) as excinfo:
            self.url_match(francis_list_url)
        assert excinfo.match(r'/lists/.+')
        assert francis_list_url != edith_list_url

        # 에디스가 입력한 흔적이 없다는 것을 다시 확인
        page_text = self.browser.find_element_by_tag_name('body').text
        assert '공작깃털 사기' not in page_text
        assert '우유 사기' in page_text

        assert 0, "Finish the test!"


if __name__ == '__main__':
    unittest.main(warnings='ignore')