# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages import MainPage, EditTopicPage, TopicsPage, ViewTopicPage, LoginPage

USERNAME = u'Владимир Мижуев'
USEREMAIL = 'ftest5@tech-mail.ru'
PASSWORD = os.environ['TTHA2PASSWORD']
BLOG = 'Флудилка'
TITLE = u'ТиПо ЗаГоЛоВоК'
SHORT_TEXT = u'Короткий текст, отображается в блогах!'
MAIN_TEXT = u'Текст под катом! Отображается внутри топика!'

def auth(driver, email=USEREMAIL, password=PASSWORD, username=USERNAME):
    auth_page = LoginPage.Page(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.open_form()
    auth_form.set_login(email)
    auth_form.set_password(password)
    auth_form.submit()

    main_page = MainPage.Page(driver)
    user_name = main_page.top_menu.get_username()
    if username == user_name:
        return True
    return False

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
        self.assertTrue(auth(self.driver))

    def test_create_delete_topic(self):
        self.assertTrue(auth(self.driver))

        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertEqual(SHORT_TEXT,blog_page.topic.get_text())

        self.assertTrue(delete_topic(self.driver))
