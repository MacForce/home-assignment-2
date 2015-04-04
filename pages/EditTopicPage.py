# coding: utf-8
from Page import Component, BasicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class Page(BasicPage):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateForm(self.driver)

class CreateForm(Component):
    BLOG_SELECT = '//a[@class="chzn-single"]'
    BLOG = '//li/em[contains(text(),"%s")]'
    TITLE = '//input[@name="title"]'
    TEXT_FIELD = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'
    TOOLBAR = '//div[@id="markItUpId_text"]//a[text()="{}"]'.decode()
    UNORDER_LIST = '//div[@id="markItUpId_text"]//li[@class="markItUpButton markItUpButton10 editor-ul"]//a[text()="Список"]'
    ORDER_LIST = '//div[@id="markItUpId_text"]//li[@class="markItUpButton markItUpButton11 editor-ol"]//a[text()="Список"]'
    SEARCH_USER_INPUT = '//div[@id="popup-search-user"][1]//input[@id="search-user-login-popup"]'
    SEARCH_USER_SUBMIT = '//div[@id="popup-search-user"][1]//input[@type="submit"]'
    ANSWER = '//div[@class="poll-create"]//input[@id="id_form-{}-answer" and @type="text"]'

    def set_blog(self, blog):
        self.driver.find_element_by_xpath(self.BLOG_SELECT).click()
        self.driver.find_element_by_xpath('//div[@class="chzn-search"]/input').send_keys(blog)
        self.driver.find_element_by_xpath(self.BLOG % blog).click()

    def set_title(self,title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_text(self,text):
        text_field = self.driver.find_element_by_xpath(self.TEXT_FIELD)
        text_field.clear()
        text_field.send_keys(text)

    def set_text_emulate(self,text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    def get_editor_text(self):
        return self.driver.find_element_by_xpath(self.TEXT_FIELD).get_attribute("value")

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()

    def set_text_h4(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('H4'.decode('utf-8'))).click()

    def set_text_h5(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('H5'.decode('utf-8'))).click()

    def set_text_h6(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('H6'.decode('utf-8'))).click()

    def set_text_bold(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('жирный'.decode('utf-8'))).click()

    def set_text_italic(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('курсив'.decode('utf-8'))).click()

    def set_text_stroke(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('зачеркнутый'.decode('utf-8'))).click()

    def set_text_underline(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('подчеркнутый'.decode('utf-8'))).click()

    def set_text_quote(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('цитировать'.decode('utf-8'))).click()

    def set_text_code(self):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('код'.decode('utf-8'))).click()

    def set_text_unordered_list(self):
        self.driver.find_element_by_xpath(self.UNORDER_LIST).click()

    def set_text_ordered_list(self):
        self.driver.find_element_by_xpath(self.ORDER_LIST).click()

    def set_text_insert_image(self, img_url, align='нет', option='', download=False):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('изображение'.decode('utf-8'))).click()
        self.driver.find_element_by_xpath('//a[text()="Из интернета"]').click()
        self.driver.find_element_by_xpath('//input[@id="img_url"]').send_keys(img_url)
        self.driver.find_element_by_xpath(
            '//select[@id="form-image-url-align"]/option[text()="{}"]'.decode().format(align.decode('utf-8'))).click()
        self.driver.find_element_by_xpath('//input[@id="form-image-url-title"]').send_keys(option)
        if download:
            self.driver.find_element_by_xpath('//button[@id="submit-image-upload-link-upload"]').click()
        else:
            self.driver.find_element_by_xpath('//button[@id="submit-image-upload-link"]').click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="window_upload_img"]'))
        )

    def set_text_load_image(self, img_path, align='нет', option=''):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('изображение'.decode('utf-8'))).click()
        self.driver.find_element_by_xpath('//a[text()="С компьютера"]').click()
        self.driver.find_element_by_xpath('(//input[@id="img_file"])').send_keys(img_path)
        self.driver.find_element_by_xpath(
            '//select[@id="form-image-align"]/option[text()="{}"]'.decode().format(align.decode('utf-8'))).click()
        self.driver.find_element_by_xpath('//input[@id="form-image-title"]').send_keys(option)
        self.driver.find_element_by_xpath('//button[@id="submit-image-upload"]').click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="window_upload_img"]'))
        )

    def set_text_link(self, link):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('Ссылка'.decode('utf-8'))).click()
        WebDriverWait(self.driver, 30, 0.1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()


    def set_text_insert_user(self, user, user_path):
        self.driver.find_element_by_xpath(self.TOOLBAR.format('Пользователь'.decode('utf-8'))).click()
        input_field = self.driver.find_element_by_xpath(self.SEARCH_USER_INPUT)
        input_field_value = input_field.get_attribute('value')
        if input_field_value == '':
            input_field.send_keys(user.decode('utf-8'))
        self.driver.find_element_by_xpath(self.SEARCH_USER_SUBMIT).click()
        user_ref = '//p[@class="realname"]//a[@href="{}"]'.format(user_path)
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, user_ref))
        )
        self.driver.find_element_by_xpath(user_ref).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="popup-search-user"]'))
        )

    def test_preview(self):
        self.driver.find_element_by_xpath('//button[@id="submit_preview"]').click()
        return WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@id="text_preview"]').is_displayed()
        )

    def set_forbid_comment(self):
        self.driver.find_element_by_xpath('//input[@name="forbid_comment"]').click()

    def set_add_poll(self, question, answers):
        self.driver.find_element_by_xpath('//input[@name="add_poll"]').click()
        self.driver.find_element_by_xpath('//div[@class="poll-create"]//input[@id="id_question"]').send_keys(question)
        if len(answers) > 2:
            for i in range(len(answers) - 2):
                self.driver.find_element_by_xpath('//a[contains(@class, "add-poll-answer")]').click()
        for n, ans in enumerate(answers):
            self.driver.find_element_by_xpath(self.ANSWER.format(n)).send_keys(ans)

    def set_remove_answer(self):
        self.driver.find_element_by_xpath(
            '//li[@class="poll-answer-container"][{}]//a[@class="remove-poll-answer icon-synio-remove"]'.format(3)).click()
        return len(self.driver.find_elements_by_xpath(self.ANSWER.format(2))) == 0

    def is_error(self):
        return WebDriverWait(self.driver, 2, 0.1).until(
            lambda d: d.find_element(By.CLASS_NAME, 'system-message-error').is_displayed()
        )