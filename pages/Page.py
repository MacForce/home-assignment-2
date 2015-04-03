# coding: utf-8
import urlparse

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class BasicPage(Component):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    PATH = ''

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()