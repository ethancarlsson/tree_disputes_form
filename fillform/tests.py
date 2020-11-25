from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_there_is_homepage(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Fill in your form', self.browser.page_source)

    def test_fillform(self):
        self.browser.get('http://127.0.0.1:8000')
        fill_form_button = self.browser.find_element_by_xpath('/html/body/div/a')
        fill_form_button.click()
        self.assertIn('Do you have', self.browser.page_source)
    
    def test_all_buttons(self):
        self.browser.get('http://127.0.0.1:8000/fillform')
        radio_buttons = self.browser.find_elements_by_id('choice.id')
        for element in radio_buttons: 
            element.click()

        self.browser.find_element_by_xpath('/html/body/ul/form/input[14]').click()
        self.assertIn('Form C', self.browser.page_source)


    def tearDown(self):
        self.browser.quit()

class UnitTest(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'fillform/home.html')

        