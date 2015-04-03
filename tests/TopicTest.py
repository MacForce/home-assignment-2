# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages import EditTopicPage, TopicsPage, ViewTopicPage
from MainTest import auth, delete_topic, BLOG, TITLE, SHORT_TEXT, MAIN_TEXT

class TopicTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        try:
            self.assertTrue(auth(self.driver))
        except AssertionError:
            self.driver.quit()
            raise

    def tearDown(self):
        try:
            self.assertTrue(delete_topic(self.driver, TITLE))
        finally:
            self.driver.quit()

    def test_max_title_len(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        max_title = 'a' * 250
        create_form.set_title(max_title)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(max_title,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(max_title,blog_page.topic.get_title())
        self.assertEqual(SHORT_TEXT,blog_page.topic.get_text())

    def test_bold_short_and_italic_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_bold_short_text()
        create_form.set_text_emulate(SHORT_TEXT)
        create_form.set_italic_main_text()
        create_form.set_text_emulate(MAIN_TEXT)
        create_form.submit()
        # time.sleep(30)
        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_italic(MAIN_TEXT))
        # time.sleep(30)
        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_bold(SHORT_TEXT))

    def test_quote_short_and_unordered_list_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_quote_short_text()
        create_form.set_text_emulate(SHORT_TEXT)
        create_form.set_unordered_list_main_text()
        create_form.set_text_emulate(MAIN_TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_unordered_list(MAIN_TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_quote(SHORT_TEXT))

    def test_ordered_list_short_and_link_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_ordered_list_short_text()
        create_form.set_text_emulate(SHORT_TEXT)
        create_form.set_link_main_text('http://example.com/')
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_link('http://example.com/'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_ordered_list(SHORT_TEXT))

    def test_insert_image_short_and_load_image_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_insert_image_short_text('http://example.com/some_img.jpg')
        create_form.set_load_image_main_text('/path_to/image.jpg')
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_text_contains_img('image.jpg'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_text_contains_external_img('http://example.com/some_img.jpg'))

    # пришлось тестировать по отдельности, тк в один пост почему то нельзя добавить юзера и в текст и в краткий текст
    def test_insert_user_short_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_insert_user_short_text(u'якимов', '/profile/m.yakimov/')
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_text_contains_user_ref('/profile/m.yakimov/'))

    def test_insert_user_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_insert_user_main_text(u'якимов', '/profile/m.yakimov/')
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_text_contains_user_ref('/profile/m.yakimov/'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertEqual(SHORT_TEXT,blog_page.topic.get_text())

    def test_forbid_comment(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.set_forbid_comment()
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_forbid_comment())

    def test_add_poll(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.set_add_poll('question', ['answer_1', 'answer_2'])
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_poll(['answer_1', 'answer_2']))

    def test_add_poll_add_answer(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.set_add_poll('question', ['answer_1', 'answer_2', 'answer_3'])
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(MAIN_TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_poll(['answer_1', 'answer_2', 'answer_3']))

class TopicNotCreateTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        try:
            self.assertTrue(auth(self.driver))
        except AssertionError:
            self.driver.quit()
            raise

    def tearDown(self):
        self.driver.quit()

    def test_add_poll_remove_adding_answer(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        self.assertTrue(create_form.test_add_poll_remove_answer())

    def test_empty_blog(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_too_long_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title('a' * 251)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_short_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_main_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_add_poll_question(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.set_add_poll('', ['answer_1', 'answer_2'])
        create_form.submit()

        self.assertTrue(create_form.is_error())

    def test_empty_add_poll_answer(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.set_add_poll('question', ['answer_1'])
        create_form.submit()

        self.assertTrue(create_form.is_error())