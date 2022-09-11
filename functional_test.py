from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        # User opens the website
        self.browser.get('http://localhost:8000')

        # Check that it is the right page, called 'To-Do List'
        self.assertIn('To-Do List', self.browser.title)
        self.fail('Finish the test!')
        
        # Register the first to-do item, in a blank space, hit enter and it creates a new line to add a new to-do item
        
        # User sees a message that his to-do items were automatically saved
        
        # Refresh the page to certify that the items were saved
        
        # User closes the page

if __name__ == '__main__':
    unittest.main(warnings='ignore')
