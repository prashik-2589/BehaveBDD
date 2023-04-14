import time
# import allure_behave
# import allallure_reports
# import allure
from behave import *
import webdriver_manager
import selenium
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By


@given(u'I have navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\python projects\driver\chromedriver.exe")
    context.driver.get("https://www.google.com/")
    context.driver.implicity_wait(5)



@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    assert "Google" in title
    print(title)



@then(u'I enter text "{search_text}"')
def step_impl(context,search_text):
    context.driver.find_element(By.NAME,"q").send_keys(search_text)



@then(u'I click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
    time.sleep(2)
