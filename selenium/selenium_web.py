from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https:github.com")

# finding element by text
sign_in_link = browser.find_element_by_link_text("Sign in")

# clicking that element
sign_in_link.click()

# finding element on webpage and select it using class name
username_box = browser.find_element_by_id("login_field")

# stimulating a user typing text
username_box.send_keys("plathia1998@gmail.com")

