from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@given(u'I go to google home page')
def step_impl(context):
	context.driver.get('https://www.google.com.br/')

@then(u'I search for a dog')
def step_impl(context):
	context.driver.implicitly_wait(5)
	context.driver.find_element_by_name('q').send_keys('dog')

@then(u'I click on google search button')
def step_impl(context):
	context.driver.find_element_by_class_name('Tg7LZd').click()

@then(u'I should see a search for dogs')
def step_impl(context):
	pass
