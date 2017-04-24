from selenium import webdriver
import unittest


# unittest code in Test-Driven Development with Python
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('To-Do', self.browser.title)


# pytest code
class TestNewVisitor(object):

    def test_show_title(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get('http://localhost:5000')
        assert 'To-Do' in browser.title
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')