import selenium
from selenium import webdriver
import time

def solutions_page():
    
    #Launch the website, Click on ‘Solutions’ navigation menu from the top and then HR Core
    driver.get("https://elmosoftware.com.au/")
     
    solutions_button = driver.find_element_by_xpath("(//a[text()='Solutions'])[1]")
    solutions_button.click()    
   
    hrCore_button = driver.find_element_by_xpath("(//div[text()='HR Core'])[2]")    
    hrCore_button.click()

    #Verify that the URL is https://elmosoftware.com.au/solutions/core-hr/
    expected_url = "https://elmosoftware.com.au/solutions/core-hr/"
    current_url = driver.current_url
    if (expected_url == current_url):
        print ("The url of the webpage is as expected. The url is %s" %current_url)
    else:
        print ("Error - The url is not as expected")
    
    #Verify that the text ‘Key Benefits’ exists in the page
    text = "Key Benefits"
    if (text in driver.page_source):
        print ("Key Benefits exists on page")
    else:
        print ("Error - Key Benefits does not exist on page")
    
    #Navigate to Payroll menu using the dropdown
    driver.find_element_by_id('select2-select-product-container').click()
    time.sleep(2)
    payroll_dropdown = driver.find_element_by_xpath("//li[text()='Payroll']")
    payroll_dropdown.click()

    #Verify that the text ‘Seamless cloud-based payroll and HR solution’ exists in the page
    text = "Seamless cloud-based payroll and HR solution"
    if (text in driver.page_source):
        print ("Seamless cloud-based payroll and HR solution exists on page")
    else:
        print ("Error - Seamless cloud-based payroll and HR solution does not exist on page")
    
    
    return

def careers_page():
    
    #Launch the website and verify Browse Jobs button exists on page
    driver.get("https://elmosoftware.com.au/careers")
    driver.maximize_window()
    if driver.find_element_by_xpath("//a[text()='Browse Jobs']"):
        print ("Browse Jobs button exists")
    else:
        print ("Error - Browse Jobs button does not exist on page")

    #Launch jobs webpage, search for PHP jobs in Sydney location
    driver.get("https://elmosoftware.com.au/jobs")
    iframe = driver.find_element_by_id('elmo-recruitment-embed')
    driver.switch_to.frame(iframe)
    
    search_jobs_box = driver.find_element_by_id('search-text')
    search_jobs_box.send_keys('PHP')
    
    job_location_dropdown = driver.find_element_by_css_selector("button[title='Select Job Location']")
    job_location_dropdown.click()
    
    sydney_checkbox = driver.find_element_by_xpath("//label[@class='checkbox']/span[contains(text(),'Sydney')]")
    sydney_checkbox.click()

    search_button = driver.find_element_by_css_selector("button[title='Search']")
    search_button.click()
    time.sleep(2)

    #Verify that the returned result contains the requested job
    text = "Senior PHP Software Engineer"
    if (text in driver.page_source):
        print ("Senior PHP Software Engineer exists on page")
    else:
        print ("Error - Senior PHP Software Engineer does not exist on page")
       
    driver.switch_to.default_content()
    return
    
if __name__ == "__main__":
    driver = webdriver.Chrome()
    solutions_page()
    careers_page()
    driver.close()
    
