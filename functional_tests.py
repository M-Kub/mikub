from selenium import webdriver
import unittest


class CheckWebsiteDesignTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visitor_comes_to_site(self):
        self.browser.get('http://localhost:8000/webblog')
        self.assertIn('Mikub Coding', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
