# coding: utf-8
from Page import BasicPage, Component
from selenium.webdriver.support.ui import WebDriverWait

class Page(BasicPage):
    PATH = '/feed/'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )