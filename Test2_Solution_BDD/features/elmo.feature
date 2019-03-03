Feature: Elmo website actions
Navigating through the Elmo website and verifying different actions
	
Scenario: Navigating HR Core page under Solutions page
Given the user visits http://elmosoftware.com.au/ webpage
When the user clicks on Solutions navigation menu 
And the user clicks on HR Core
Then the url will be https://elmosoftware.com.au/solutions/core-hr/ 
And the text Key Benefits exists in the page
 
Scenario: Navigating to Payroll page
Given the user is in https://elmosoftware.com.au/solutions/core-hr/ page
When user clicks on the dropdown menu at the top beside ‘Learn about another product’
And clicks on Payroll from the dropdown menu
Then the text ‘Seamless cloud-based payroll and HR solution’ exists in the page
 
Scenario: Navigating Careers page
When the user visits https://elmosoftware.com.au/careers/ in the browser
Then the user checks if Browse Jobs button exists in the webpage

Scenario: Navigating Jobs page
Given the user visits https://elmosoftware.com.au/jobs/
When the user enters the text PHP in search text field under Search Jobs section 
And the user selects Sydney checkbox under All Locations dropdown
And the user clicks on Search icon beside Search text field
Then Senior PHP Software Engineer job exists in the page