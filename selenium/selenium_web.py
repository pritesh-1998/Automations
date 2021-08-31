import details
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https:github.com")

# finding element by text
sign_in_link = browser.find_element_by_link_text("Sign in")

# clicking that element
sign_in_link.click()

# finding element on webpage and select it using class name
username_box = browser.find_element_by_id("login_field")
password_box = browser.find_element_by_id("password")

# stimulating a user typing text
username_box.send_keys(details.username)
password_box.send_keys(details.password)
password_box.submit()


