# coding: utf-8
from Page import BasicPage
from TopicsPage import Topic

class Page(BasicPage):
    @property
    def topic(self):
        return Topic(self.driver)
