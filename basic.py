from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.qa-practice.com/elements/button/simple')
# click_button = browser.find_element(By.ID, 'submit-id-submit')
# click_button.click()
# click_button2 = browser.find_element(By.CLASS_NAME, 'btn-primary')
# click_button2.click()

click_button2 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
click_button2.click()

# link = browser.find_element(By.LINK_TEXT, 'Contact')
# link.click()

sleep(5)
