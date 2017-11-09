from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


# pytest code
class TestNewVisitor(object):
    @staticmethod
    def url_match(url):
        raise ValueError(url)

    # using fixture set_browser in conftest.py
    @pytest.mark.skip
    def test_layout_and_styling(self, browser):
        # 에디스는 메인 페이지를 방문한다.
        browser.get('http://localhost:5000')
        browser.set_window_size(1024, 768)

        inputbox = browser.find_element_by_id('id_new_item')

        location_value = inputbox.location['x'] + inputbox.size['width'] / 2

        assert 500 < location_value < 530

    # def test_cannot_add_empty_list_items(self):
    #     # 에디스는 메인 페이지에 접속해서 빈 아이템을 실수로 등록하려고 한다
    #     # 입력 상자가 비어 있는 상태에서 엔터키를 누른다
    #
    #     # 페이지가 새로고침되고 빈 아이템을 등록할 수 없다는 에러 메시지가 표시된다
    #     # 다른 아이템을 입력하고 이번에는 정상 처리된다
    #     # 그녀는 고의적으로 다시 빈 아이템을 등록
    #     # 리스트 페이지에 다시 에러 메시지 표시
    #     # 아이템을 입력하면 정상 동작한다
    #     self.fail('write me!')

    @pytest.mark.skip
    def test_show_title(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get('http://localhost:5000')
        assert 'To-Do' in self.browser.title

        header_text = self.browser.find_element_by_tag_name('h1').text
        assert '작업 목록' in header_text

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

        page_text = self.browser.find_element_by_tag_name('body').text
        assert '공작깃털 사기' in page_text
        assert '그물 만들기' in page_text

        # 프란시스가 새로운 작업 아이템을 입력하기 시작한다.
        self.browser.get('http://localhost:5000')
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
