# coding: utf-8
from Page import BasicPage, Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
            lambda d: d.find_element_by_xpath(self.TEXT.format('')).text
        )

    def is_h4(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/h4')).text):
            return True
        return False

    def is_h5(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/h5')).text):
            return True
        return False

    def is_h6(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/h6')).text):
            return True
        return False

    def is_bold(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/strong')).text):
            return True
        return False

    def is_italic(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/em')).text):
            return True
        return False

    def is_stroke(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/s')).text):
            return True
        return False

    def is_underline(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/u')).text):
            return True
        return False

    def is_quote(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/blockquote')).text):
            return True
        return False

    def is_code(self, text):
        if text == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/code')).text):
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
                lambda d: d.find_element_by_xpath(self.TEXT.format('/a')).get_attribute('href')):
            return True
        return False

    def is_img(self, img_name, align=None, title=None):
        WebDriverWait(self.driver, 30, 0.1).until(
                EC.visibility_of_element_located((By.XPATH, self.TEXT.format('/img'))))
        img_tag = self.driver.find_element_by_xpath(self.TEXT.format('/img'))
        if img_name in img_tag.get_attribute('src'):
            if align is not None and align != img_tag.get_attribute('align'):
                if align == 'center':
                    if 'middle' != img_tag.get_attribute('align'):
                        return False
                else:
                    return False
            if title is not None and title != img_tag.get_attribute('title'):
                return False
            return True
        return False

    def is_text_contains_user_ref(self, user_path):
        if 'http://ftest.stud.tech-mail.ru{}'.format(user_path) == WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(self.TEXT.format('/a')).get_attribute('href')):
            return True
        return False

    def is_forbid_comment(self):
            return len(self.driver.find_elements_by_xpath('//h4[@class="reply-header"]')) == 0

    def is_poll(self, answers):
        for i, ans in enumerate(answers):
            if ans not in self.driver.find_element_by_xpath('//ul[@class="poll-vote"]/li[{}]'.format(i + 1)).text:
                return False
        return True

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.DELETE_BUTTON_CONFIRM))
        )
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()