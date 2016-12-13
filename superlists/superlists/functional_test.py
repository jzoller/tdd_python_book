from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (her hobby is tying fly-fishing lures)

        # When she hits enter, the page updates and lists "1: Buy peacock feathers" as an item in a to-do list

        # There still a textbox to add another item
        # She enters "Use peacock feathers to make a fly"

        # Page updates again and shows both items on her list

        # Edith wonders whetherthe site will remember her list. Then she sees that the site has generated
        # a unique url for her and there is some text to that effect.

        # She visits that URL- her to-do list is still there.
if __name__ == '__main__':
    unittest.main(warnings='ignore')

