# coding: utf-8
from Page import BasicPage, Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Page(BasicPage):
    PATH = '/blog/show/2544/fludilka/'

    @property
    def topic(self):
        return Topic(self.driver)

class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//article[@class="topic topic-type-topic js-topic"][1]//*[@class="topic-content text"]{}'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/p')).text
        )

    def is_bold(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/strong')).text):
            return True
        return False

    def is_italic(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/em')).text):
            return True
        return False

    def is_quote(self, text):
        real_text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/p')).text)
        if text in real_text and real_text.startswith('>'):
            return True
        return False

    def is_ordered_list(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/ol/li')).text):
            return True
        return False

    def is_unordered_list(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/ul/li')).text):
            return True
        return False

    def is_link(self, url):
        if url == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/a')).get_attribute('href')):
            return True
        return False

    def is_text_contains_img(self, img_name):
        if img_name in WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/img')).get_attribute('src')):
            return True
        return False

    def is_text_contains_external_img(self, img_url):
        if img_url == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/img')).get_attribute('src')):
            return True
        return False

    def is_text_contains_user_ref(self, user_path):
        if 'http://ftest.stud.tech-mail.ru{}'.format(user_path) == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/p/a')).get_attribute('href')):
            return True
        return False

    def is_forbid_comment(self):
        try:
            WebDriverWait(self.driver, 2, 0.1).until(lambda d: d.find_element_by_xpath('//h4[@class="reply-header"]'))
            return False
        except TimeoutException as ignore:
            return True

    def is_poll(self, answers):
        i = 1
        for ans in answers:
            if ans not in self.driver.find_element_by_xpath('//ul[@class="poll-vote"]/li[{}]'.format(i)).text:
                return False
            i += 1
        return True

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()