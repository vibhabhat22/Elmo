from behave import *

#Scenario: Navigating HR Core page under Solutions page
@given("the user visits http://elmosoftware.com.au/ webpage")
def user_on_elmo_page(context):	
    context.web.get("http://elmosoftware.com.au/")
	
@when("the user clicks on Solutions navigation menu")
def user_on_solutions_page(context):
    context.web.find_element_by_xpath("(//a[text()='Solutions'])[1]").click()
	
@when("the user clicks on HR Core")
def user_on_hrcore_page(context):
    context.web.find_element_by_xpath("(//div[text()='HR Core'])[2]").click()
	
@then("the url will be https://elmosoftware.com.au/solutions/core-hr/")
def validate_hrcore_url(context):
    assert context.web.current_url == "https://elmosoftware.com.au/solutions/core-hr/"
	
@then("the text Key Benefits exists in the page")
def validate_KBtext_on_page(context):
	assert context.web.page_source == "Key Benefits"
	

#Scenario: Navigating to Payroll page
@given("the user is in https://elmosoftware.com.au/solutions/core-hr/ page")
def user_on_hrcore_page_payroll(context):
	context.web.get("https://elmosoftware.com.au/solutions/core-hr/")
	
@when("user clicks on the dropdown menu at the top beside ‘Learn about another product’")
def user_clicks_dropdown(context):
	context.web.find_element_by_id('select2-select-product-container').click()
	
@when("clicks on ‘Payroll’ from the dropdown menu")
def user_clicks_payroll(context):
	context.web.find_element_by_xpath("//li[text()='Payroll']").click()
	
@then("the text ‘Seamless cloud-based payroll and HR solution’ exists in the page")
def user_on_payroll_page(context):
	assert context.web.page_source == "Seamless cloud-based payroll and HR solution"
	
#Scenario: Navigating Careers page
@when("the user visits https://elmosoftware.com.au/careers/ in the browser")
def user_on_careers_page(context):
	context.web.get("https://elmosoftware.com.au/careers/")
	
@then("the user checks if 'Browse Jobs' button exists in the webpage")
def user_browse_jobs_button(context):
	assert context.web.page_source == "Browse Jobs"
	
#Scenario: Navigating Jobs page
@given("the user visits https://elmosoftware.com.au/jobs/")
def user_on_jobs_page(context):
	context.web.get("https://elmosoftware.com.au/jobs/")
	
@when("the user enters the text ‘PHP' in search text field under ‘Search Jobs’ section")
def search_jobs_field_input(context):
	search_jobs_box = context.web.find_element_by_id('search-text')
	search_jobs_box.send_keys('PHP')
	
@when("the user selects Sydney checkbox under All Locations dropdown")
def location_checkbox_input(context):
	job_location_dropdown = context.web.driver.find_element_by_css_selector("button[title='Select Job Location']")
	job_location_dropdown.click()
	context.web.find_element_by_xpath("//label[@class='checkbox']/span[contains(text(),'Sydney')]").click()
	
@when("the user clicks on Search icon beside Search text field")
def search_icon_click(context):
	context.web.find_element_by_css_selector("button[title='Search']").click()
	
@then("Senior PHP Software Engineer job exists in the page")
def validate_job_output(context):
	assert context.web.page_source == "Senior PHP Software Engineer"


	
	
	