from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# check out online to-do app homepage
		self.browser.get('http://localhost:8000')
		#@ notices the page title and header mention to-do lists
		self.assertIn('To-do', self.browser.title)
		self.fail('finish the test!')

if __name__ == "__main__":
	unittest.main(warnings='ignore')