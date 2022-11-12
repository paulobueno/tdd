import selenium.webdriver.firefox.options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        options = selenium.webdriver.firefox.options.Options()
        options.binary_location = '/usr/local/bin/firefox'
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        # User opens the website
        self.browser.get('http://localhost:8000')

        # Check that it is the right page, called 'To-Do List' and header 'To-Do'
        self.assertIn('To-Do List', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Register the first to-do item, in a blank space, hits enter, and it creates a new line to add a new to-do item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Writes 'Buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')

        # Hits enter and a new line is created
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # Check if there still exists an input box
        # Add second item and check if it was correctly registered
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])


        # User sees a message that his to-do items were automatically saved
        self.fail('Finish the test!')

        # Refresh the page to certify that the items were saved


        # User closes the page



if __name__ == '__main__':
    unittest.main(warnings='ignore')
