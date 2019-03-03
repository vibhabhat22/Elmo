from selenium import webdriver

def before_all(context):
    context.web = webdriver.Chrome("C:/chromedriver.exe")