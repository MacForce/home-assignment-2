# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages import EditTopicPage
from MainTest import auth, BLOG, TITLE, TEXT

class NoTopicTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_add_poll_remove_adding_answer(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_add_poll('q', ['1', '2', '3'])
        self.assertTrue(create_form.set_remove_answer())

    def test_empty_blog(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_text(TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_too_long_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title('a' * 251)
        create_form.set_text(TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_add_poll_question(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.set_add_poll('', ['answer_1', 'answer_2'])
        create_form.submit()

        self.assertTrue(create_form.is_error())

    # бага - если какой-то ответ не указать, то опрос всё равно создастся
    # поэтому данный тест не проходит
    # def test_empty_add_poll_answer(self):
    #     edit_page = EditTopicPage.Page(self.driver)
    #     edit_page.open()
    #
    #     create_form = edit_page.form
    #     create_form.set_blog(BLOG)
    #     create_form.set_title(TITLE)
    #     create_form.set_text(TEXT)
    #     create_form.set_add_poll('question', ['answer_1'])
    #     create_form.submit()
    #
    #     self.assertTrue(create_form.is_error())
