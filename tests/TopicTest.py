# coding: utf-8
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages import EditTopicPage, TopicsPage, ViewTopicPage
from MainTest import auth, delete_topic, BLOG, TITLE, TEXT

EXTERNAL_IMG = 'www.google.ru/intl/en_ALL/images/srpr/logo11w.png'
MAX_TITLE = 'a' * 250

class TopicTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth(self.driver)

    def tearDown(self):
        try:
            self.assertTrue(delete_topic(self.driver, TITLE))
        finally:
            self.driver.quit()

    def test_max_title_len(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(MAX_TITLE)
        create_form.set_text(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(MAX_TITLE,topic_page.topic.get_title())
        self.assertEqual(TEXT,topic_page.topic.get_text())

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(MAX_TITLE,blog_page.topic.get_title())
        self.assertEqual(TEXT,blog_page.topic.get_text())

    def test_h4_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_h4()
        self.assertEqual(create_form.get_editor_text(),'<h4></h4>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_h4(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_h4(TEXT))

    def test_h5_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_h5()
        self.assertEqual(create_form.get_editor_text(),'<h5></h5>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_h5(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_h5(TEXT))

    def test_h6_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_h6()
        self.assertEqual(create_form.get_editor_text(),'<h6></h6>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_h6(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_h6(TEXT))

    def test_bold_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_bold()
        self.assertEqual(create_form.get_editor_text(),'<strong></strong>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_bold(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_bold(TEXT))

    def test_italic_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_italic()
        self.assertEqual(create_form.get_editor_text(),'<em></em>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_italic(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_italic(TEXT))

    def test_stroke_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_stroke()
        self.assertEqual(create_form.get_editor_text(),'<s></s>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_stroke(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_stroke(TEXT))

    def test_underline_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_underline()
        self.assertEqual(create_form.get_editor_text(),'<u></u>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_underline(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_underline(TEXT))

    # бага - курсор ставится после тегов
    def test_quote_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_quote()
        self.assertEqual(create_form.get_editor_text(),'<blockquote></blockquote>')

        quote = u'<blockquote>{}</blockquote>'
        create_form.set_text(quote.format(unicode(TEXT)))
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_quote(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_quote(TEXT))

    def test_code_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_code()
        self.assertEqual(create_form.get_editor_text(),'<code></code>')

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_code(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_code(TEXT))

    def test_unordered_list_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_unordered_list()

        unorder_list = ['<ul>','<li></li>','</ul>']
        self.assertTrue(all(x in create_form.get_editor_text() for x in unorder_list))

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_unordered_list(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_unordered_list(TEXT))

    def test_ordered_list_text(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_ordered_list()

        order_list = ['<ol>','<li></li>','</ol>']
        self.assertTrue(all(x in create_form.get_editor_text() for x in order_list))

        create_form.set_text_emulate(TEXT)
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_ordered_list(TEXT))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_ordered_list(TEXT))

    def test_load_image(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_load_image(os.getcwd() + '/my_img.jpg')

        img = ['<img','my_img']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('my_img'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('my_img'))

    def test_load_image_with_align(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_load_image(os.getcwd() + '/my_img.jpg', align='по центру')

        img = ['<img','my_img', 'align="center"']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('my_img', align='center'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('my_img', align='center'))

    def test_load_image_with_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_load_image(os.getcwd() + '/my_img.jpg', option='1234567890')

        img = ['<img','my_img', 'title="1234567890"']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('my_img', title='1234567890'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('my_img', title='1234567890'))

    def test_insert_image_and_download(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_insert_image(EXTERNAL_IMG, download=True)

        img = ['<img','.png']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('.png'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('.png'))

    def test_insert_image(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_insert_image(EXTERNAL_IMG)

        img = ['<img','http://' + EXTERNAL_IMG]
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('http://'+EXTERNAL_IMG))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('http://'+EXTERNAL_IMG))

    def test_insert_image_with_align(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_insert_image(EXTERNAL_IMG, align='по центру')

        img = ['<img','http://'+EXTERNAL_IMG, 'align="center"']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('http://'+EXTERNAL_IMG, align='center'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('http://'+EXTERNAL_IMG, align='center'))

    def test_insert_image_with_title(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_insert_image(EXTERNAL_IMG, option='1234567890')

        img = ['<img','http://'+EXTERNAL_IMG, 'title="1234567890"']
        self.assertTrue(all(x in create_form.get_editor_text() for x in img))

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_img('http://'+EXTERNAL_IMG, title='1234567890'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_img('http://'+EXTERNAL_IMG, title='1234567890'))

    def test_link(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_link('http://example.com/')
        self.assertTrue('href="http://example.com/"' in create_form.get_editor_text())

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_link('http://example.com/'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_link('http://example.com/'))

    def test_insert_user(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text_insert_user('якимов', '/profile/m.yakimov/')

        self.assertTrue('href="/profile/m.yakimov/"' in create_form.get_editor_text())

        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertTrue(topic_page.topic.is_text_contains_user_ref('/profile/m.yakimov/'))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertTrue(blog_page.topic.is_text_contains_user_ref('/profile/m.yakimov/'))

    def test_forbid_comment(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.set_forbid_comment()
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_forbid_comment())

    def test_add_poll(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.set_add_poll('question', ['answer_1', 'answer_2'])
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_poll(['answer_1', 'answer_2']))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertEqual(TEXT,blog_page.topic.get_text())
        self.assertTrue(blog_page.topic.is_poll(['answer_1', 'answer_2']))

    def test_add_poll_add_answer(self):
        edit_page = EditTopicPage.Page(self.driver)
        edit_page.open()

        create_form = edit_page.form
        create_form.set_blog(BLOG)
        create_form.set_title(TITLE)
        create_form.set_text(TEXT)
        create_form.set_add_poll('question', ['answer_1', 'answer_2', 'answer_3'])
        create_form.submit()

        topic_page = ViewTopicPage.Page(self.driver)
        self.assertEqual(TITLE,topic_page.topic.get_title())
        self.assertEqual(TEXT,topic_page.topic.get_text())
        self.assertTrue(topic_page.topic.is_poll(['answer_1', 'answer_2', 'answer_3']))

        topic_page.topic.open_blog()
        blog_page = TopicsPage.Page(self.driver)
        self.assertEqual(TITLE,blog_page.topic.get_title())
        self.assertEqual(TEXT,blog_page.topic.get_text())
        self.assertTrue(blog_page.topic.is_poll(['answer_1', 'answer_2', 'answer_3']))