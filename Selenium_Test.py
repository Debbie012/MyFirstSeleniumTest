import time

import loginform
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize a new Chrome browser instance using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the CRM login page of Automation Playground
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

#Login with a valid email address
driver.find_element(By.ID, "email-id").send_keys("greenfingers@yopmail.com")
time.sleep(5)

#Enter password
driver.find_element(By.ID, "password").send_keys("cloud")
time.sleep(5)

#Click on "Remember me"
driver.find_element(By.ID, "remember").click()
time.sleep(5)

#Click the submit button
driver.find_element(By.ID, "submit-id").click()
time.sleep(5)

#Click on "New Customer" to add a new customer
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)

#Input email address of new customer
driver.find_element(By.ID, "EmailAddress").send_keys("sixtus6@yopmail.com")
time.sleep(5)

#Input first name of new customer
driver.find_element(By.ID, "FirstName").send_keys("Sixtus")
time.sleep(5)

#Input lastname of new customer
driver.find_element(By.ID, "LastName").send_keys("Afolabi")
time.sleep(5)

#Input city
driver.find_element(By.ID, "City").send_keys("Ikeja")
time.sleep(5)

#Select state
driver.find_element(By.ID, "StateOrRegion").send_keys("Texas")
time.sleep(5)

#Select gender type
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[6]/input[1]").click()
time.sleep(5)

#Check the "Add to promotional list" button
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/div[7]/input").click()
time.sleep(5)

#Click on submit
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div/div/div/form/button").click()
time.sleep(5)

#Click on Signout
driver.find_element(By.XPATH, "/html/body/nav/ul/li/a").click()
time.sleep(5)