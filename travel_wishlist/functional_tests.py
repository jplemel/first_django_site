import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import keys

from django.test import LiveServerTestCase

class FunctionalityTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_get_home_page_list_of_places(self):
        self.browser.get(self.live_server_url)

        input_name = self.browser.find_element_by_id('id_name')

        input_name.send_keys('Denver')

        add_button = self.browser.find_element_by_id('add_new_place')

        add_button.click()

        wait_for_denver = self.browser.find_element_by_id('place_name_5')

        assert 'Wishlist' in self.browser.title

        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'Denver' in self.browser.page_source


        assert 'San Francisco' not in self.browser.page_source
        assert 'Moab' not in self.browser.page_source
