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
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/h4')).text)

    def is_h5(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/h5')).text)

    def is_h6(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/h6')).text)

    def is_bold(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/strong')).text)

    def is_italic(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/em')).text)

    def is_stroke(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/s')).text)

    def is_underline(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/u')).text)

    def is_quote(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/blockquote')).text)

    def is_code(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/code')).text)

    def is_ordered_list(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/ol/li')).text)

    def is_unordered_list(self, text):
        return text == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/ul/li')).text)

    def is_link(self, url):
        return url == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/a')).get_attribute('href'))

    def is_img(self, img_name, align='', title=''):
        image = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/img'))
        )
        image_src = image.get_attribute('src')
        image_align = image.get_attribute('align')
        image_title = image.get_attribute('title')
        return img_name in image_src and align == image_align and title == image_title

    def is_text_contains_user_ref(self, user_path):
        return 'http://ftest.stud.tech-mail.ru{}'.format(user_path) == WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT.format('/a')).get_attribute('href'))

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