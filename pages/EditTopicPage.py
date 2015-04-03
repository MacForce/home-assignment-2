# coding: utf-8
import time
from Page import Component, BasicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Page(BasicPage):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateForm(self.driver)

class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    # SHORT_TEXT = '//textarea[@name="text_short"]'
    # MAIN_TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'
    ADD_TEXT_SCRIPT = u"$(\'.CodeMirror\')[{0}].CodeMirror.setValue(\"{1}\")"
    TEXT_FIELD = '//div[contains(@class, "CodeMirror cm-s-paper")][{}]//div[@class="CodeMirror-code"]/pre'
    FORMAT_TOOLBAR = '//div[@class="editor-toolbar"][{0}]//*[@class="markdown-editor-icon-{1}"{2}]'
    SEARCH_USER_INPUT = '//div[@id="popup-search-user"][1]//input[@id="search-user-login-popup"]'
    SEARCH_USER_SUBMIT = '//div[@id="popup-search-user"][1]//input[@type="submit"]'

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_title(self,title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self,short_text):
        # self.driver.find_element_by_xpath(self.SHORT_TEXT).send_keys(short_text)
        self.driver.execute_script(self.ADD_TEXT_SCRIPT.format(u'0', short_text))

    def set_text_emulate(self,short_text):
        actions = ActionChains(self.driver)
        # actions.click(self.driver.find_elements(By.CLASS_NAME, 'CodeMirror-scroll')[0])
        actions.send_keys(short_text)
        actions.perform()

    def set_main_text(self,main_text):
        # self.driver.find_element_by_xpath(self.MAIN_TEXT).send_keys(main_text)
        self.driver.execute_script(self.ADD_TEXT_SCRIPT.format(u'1', main_text))

    def get_editor_short_text(self):
        return self.driver.find_element_by_xpath(self.TEXT_FIELD.format('1')).text

    def get_editor_main_text(self):
        return self.driver.find_element_by_xpath(self.TEXT_FIELD.format('2')).text

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()

    def set_bold_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'bold', '')).click()

    def set_bold_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'bold', '')).click()

    def set_italic_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'italic', '')).click()

    def set_italic_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'italic', '')).click()

    def set_quote_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'quote', '')).click()

    def set_quote_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'quote', '')).click()

    def set_unordered_list_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'unordered-list', '')).click()

    def set_unordered_list_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'unordered-list', '')).click()

    def set_ordered_list_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'ordered-list', '')).click()

    def set_ordered_list_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'ordered-list', '')).click()

    def set_link_short_text(self, link):
        self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('1', 'link', ' and @title="Вставить ссылку"')).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def set_link_main_text(self, link):
        self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('2', 'link', ' and @title="Вставить ссылку"')).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def set_insert_image_short_text(self, link):
        self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('1', 'image', ' and @title="Вставить изображение"')).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def set_insert_image_main_text(self, link):
        self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('2', 'image', ' and @title="Вставить изображение"')).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def set_load_image_short_text(self, image_path):
        # self.driver.find_element_by_xpath(
        #     self.FORMAT_TOOLBAR.format('1', 'image', ' and @title="Загрузить изображение"')).click()
        # self.driver.find_element_by_xpath('(//input[@name="filedata"])[1]').send_keys(image_path)
        # WebDriverWait(self.driver, 30, 0.1).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '(//input[@name="filedata"])[1]')))
        # time.sleep(1)
        self.driver.execute_script(self.ADD_TEXT_SCRIPT.format(u'0', '![]({})'.format(image_path)))

    def set_load_image_main_text(self, image_path):
        # self.driver.find_element_by_xpath(
        #     self.FORMAT_TOOLBAR.format('2', 'image', ' and @title="Загрузить изображение"')).click()
        # self.driver.find_element_by_xpath('(//input[@name="filedata"])[1]').send_keys(image_path)
        # WebDriverWait(self.driver, 30, 0.1).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '(//input[@name="filedata"])[1]')))
        # time.sleep(1)
        self.driver.execute_script(self.ADD_TEXT_SCRIPT.format(u'1', '![]({})'.format(image_path)))

    def set_insert_user_short_text(self, user, user_path):
        self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('1', 'link', ' and @title="Добавить пользователя"')).click()
        input_field = self.driver.find_element_by_xpath(self.SEARCH_USER_INPUT)
        if input_field.get_attribute('value') == '':
            self.driver.find_element_by_xpath(self.SEARCH_USER_INPUT).send_keys(user)
        self.driver.find_element_by_xpath(self.SEARCH_USER_SUBMIT).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//p[@class="realname"]//a[@href="{}"]'.format(user_path)).click()
        # WebDriverWait(self.driver, 30, 0.1).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, self.SEARCH_USER_INPUT)))
        time.sleep(2)

    def set_insert_user_main_text(self, user, user_path):
        button = self.driver.find_element_by_xpath(
            self.FORMAT_TOOLBAR.format('2', 'link', ' and @title="Добавить пользователя"'))
        print button.get_attribute('innerHTML')
        button.click()
        input_field = self.driver.find_element_by_xpath(self.SEARCH_USER_INPUT)
        if input_field.get_attribute('value') == '':
            self.driver.find_element_by_xpath(self.SEARCH_USER_INPUT).send_keys(user)
        self.driver.find_element_by_xpath(self.SEARCH_USER_SUBMIT).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//p[@class="realname"]//a[@href="{}"]'.format(user_path)).click()
        # WebDriverWait(self.driver, 30, 0.1).until(
        #     expected_conditions.visibility_of_element_located((By.XPATH, self.SEARCH_USER_INPUT)))
        time.sleep(2)

    def set_preview_short_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('1', 'preview', '')).click()

    def set_preview_main_text(self):
        self.driver.find_element_by_xpath(self.FORMAT_TOOLBAR.format('2', 'preview', '')).click()

    def set_forbid_comment(self):
        self.driver.find_element_by_xpath('//input[@name="forbid_comment"]').click()

    def set_add_poll(self, question, answers):
        self.driver.find_element_by_xpath('//input[@name="add_poll"]').click()
        self.driver.find_element_by_xpath('//div[@class="poll-create"]//input[@id="id_question"]').send_keys(question)
        if len(answers) > 2:
            i = 2
            while i < len(answers):
                self.driver.find_element_by_xpath('//a[contains(@class, "add-poll-answer")]').click()
                i += 1
        i = 0
        for ans in answers:
            self.driver.find_element_by_xpath(
                '//div[@class="poll-create"]//input[@id="id_form-{}-answer" and @type="text"]'.format(i)).send_keys(ans)
            i += 1

    def test_add_poll_remove_answer(self):
        self.driver.find_element_by_xpath('//input[@name="add_poll"]').click()

        self.driver.find_element_by_xpath('//a[contains(@class, "add-poll-answer")]').click()
        self.driver.find_element_by_xpath(
            '//div[@class="poll-create"]//input[@id="id_form-{}-answer" and @type="text"]'.format(2))

        self.driver.find_element_by_xpath(
            '//li[@class="poll-answer-container"][{}]//a[@class="remove-poll-answer icon-synio-remove"]'.format(3)).click()
        try:
            self.driver.find_element_by_xpath(
                '//div[@class="poll-create"]//input[@id="id_form-{}-answer" and @type="text"]'.format(2))
            return False
        except NoSuchElementException as ignore:
            return True

    def is_error(self):
        return WebDriverWait(self.driver, 2, 0.1).until(
            lambda d: d.find_element(By.CLASS_NAME, 'system-message-error').is_displayed()
        )