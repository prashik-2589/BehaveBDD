
from behave import *
import webdriver_manager
import selenium
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By

def before_scenario(context,driver):
    context.driver = webdriver.Chrome(executable_path="D:\python projects\driver\chromedriver.exe")
def after_step(context, step):
    print()

def after_scenario(context, driver):
    context.driver.quit()