import requests
import pprint
#import getpass

##USER = input("Enter your webex teams username: ")
##PASS = getpass.getpass()
TOKEN = "OWJmMzEwMjYtZDU0Yi00OWQ5LTlhYTgtN2QyYWIzYWJiZWE4ODY5OWIwZTktNDFl_PF84_consumer"
##URL = "https://webexapis.com/v1/authorize"

APIHeaders = {'Authorization': 'Bearer ' + TOKEN,
		'Content-type': 'application/json'}

response = requests.get(URL, headers=APIHeaders)

##auth_token = response.JSON()['auth_token']

addresses = []

##defined URLs for get/post requests to webex
URL2 = "https://webexapis.com/v1/people"
URL3 = "https://wenexapis.com/v1/places"

more = input("Do you have an email to enter (y/n)? ")

while more == "y":
	email = input("Enter the address: ")
	addresses.append(email)
	more = input("Do you have another address(y/n)?: ")
	while more != "y":
		if more == "n":
		##once there are no more, creates a post request using the places URL to create a orgId
		createpage = requests.post(URL3, headers=APIHeaders)
		JSONformatted = createpage.json()
			for parameter in JSONformatted:
				#creates a variable from the orgId value
				origID = parameter['orgId']
				print("A group with the ID: " + str(orgID) + "has been created")
			break
		else:
			more = input("Please enter a y or n:")

for email in addresses:
	##creates a data form to be sent in the POST requests, pulling the emails from the lists and calling back to the origID variable created earlier
	data = {'emails' : email,
		'orgID' : origID}
	##sends the request to create a Person with parameters sent to the data header option
	createperson = requests.post(URL2, headers=APIHeaders, data = data)
	##sends a get request to retrieve the list of emails just created
	getpersonraw = requests.get(URL2, headers=APIHeaders)
	##turns the raw data into JSON readable text, then creates a variable for each key:value pair and prints each email with the OrgID variables
	getperson = getperson.json()
	for parameter2 in getperson:
		print("The email: " + str(email) + " belongs to " + str(origID))

		 
	
	



