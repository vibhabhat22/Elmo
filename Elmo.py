import boto3
import selenium
from selenium import webdriver

import time

#def solutions_page():
if __name__ == "__main__":

    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get("https://elmosoftware.com.au/")
    solution_button = driver.find_element_by_name('Solutions')
    solution_button.click()
    
