# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages import MainPage, EditTopicPage, TopicsPage, ViewTopicPage, LoginPage

USERNAME = u'Владимир Мижуев'
USEREMAIL = 'ftest5@tech-mail.ru'
PASSWORD = os.environ['TTHA2PASSWORD']
BLOG = 'Флудилка'
TITLE = u'ТиПо ЗаГоЛоВоК'
TEXT = u'Основной текст топика!'

def auth(driver, email=USEREMAIL, password=PASSWORD):
    auth_page = LoginPage.Page(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.open_form()
    auth_form.set_login(email)
    auth_form.set_password(password)
    auth_form.submit()
    WebDriverWait(driver, 30, 0.1).until(
         expected_conditions.invisibility_of_element_located((By.XPATH, '//div[@id="popup-login"]'))
    )

def delete_topic(driver, title=TITLE):
    blog_page = TopicsPage.Page(driver)
    blog_page.open()
    blog_page.topic.delete()
    topic_title = blog_page.topic.get_title()
    if title != topic_title:
        return True
    return False

class MainTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_auth(self):
        auth(self.driver)
        main_page = MainPage.Page(self.driver)
        user_name = main_page.top_menu.get_username()
        if USERNAME == user_name:
            return True
        return False

    def test_create_delete_topic(self):
        auth(self.driver)

        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.submit()

        try:
            topic_page = ViewTopicPage.Page(self.driver)
            self.assertEqual(TITLE,topic_page.topic.get_title())
            self.assertEqual(TEXT,topic_page.topic.get_text())

            topic_page.topic.open_blog()
            blog_page = TopicsPage.Page(self.driver)
            self.assertEqual(TITLE,blog_page.topic.get_title())
            self.assertEqual(TEXT,blog_page.topic.get_text())
        finally:
            self.assertTrue(delete_topic(self.driver))
