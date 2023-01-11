# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import os
from pyad import aduser
from pyad import *
import maskpass
import subprocess, sys
import pyperclip
import time
import json

# Variables
# Constants
DRIVER_PATH =  ("PATH")

# Printer 1 variables
printer1_add_button = ("xpath")
printer1_address_name_button = ("xpath")
printer1_printer_email_button = ("xpath")
printer1_default_used_box = ("xpath")
printer1_register_next_button = ("xpath")



# Printer 2 Variables
printer2_add_button = ("xpath")
printer2_address_name_button = ("xpath")
printer2_printer_email_button = ("xpath")
printer2_default_used_box = ("xpath")
printer2_submit_button = ("xpath")
printer2_register_next_button = ("xpath")



# Loads printers.json and allows selection
def json_selector(selection):

	printers = json.load(open('path\\printers.json'))
	return (printers.get(selection))



#Main Jobsite Printer Function
def jobsite_printer_selection():

	# Grabs list of names from user and converts to list
	names = []
	print("Enter user's first and last name's on seperate lines. For example: \nFirst name Last name \nFirst name Last name \nEnter answer here:") 
	while True: 
		line = input("") 
		if line == "": 
			break 
		else:
			names.append(line)
			#names = names.join(line) 




# Grabs email based off first and last name from ADS
	try:
		user_emails = []
		try:
			idx = 0
			for name in names:
				user_email = aduser.ADUser.from_cn(name).mail
				user_emails.append(user_email)
				idx += 1
		except ConnectionError as err:
			print("Could not connect to AD: {}.".format(err))
	except:
		raise Exception("Invalid Name!") 


	
	print(names)
	print(user_emails)


# Adds to printers
	while ask_user_printer <= 14:

		if ask_user_printer == 1:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("HUNTSMAN_CANCER_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for name in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(name)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break
			
		
		elif ask_user_printer == 2:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("LONE_PEAK_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 3:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("MERCY_SW_PRINTER")) 
			add = driver.find_element_by_xpath(printer1_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer1_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer1_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 4:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("SGHNC_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break
		
	

		elif ask_user_printer == 5:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("MAUI_COAST_HOTEL_PRINTER")) 
			add = driver.find_element_by_xpath(printer1_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer1_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer1_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 6:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("WORTHINGTON_TOWER_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 7:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("CAESARS_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 8:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("ST_MARKS_2_PRINTER")) 
			add = driver.find_element_by_xpath(printer1_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer1_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer1_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 9:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("BAYONET_PRINTER")) 
			add = driver.find_element_by_xpath(printer1_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer1_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer1_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break

		elif ask_user_printer == 10:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("HUB_202_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break


		elif ask_user_printer == 11:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("PENSKE_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break
		

		elif ask_user_printer == 12:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("ALIGNED_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break
	


		elif ask_user_printer == 13:
			driver = webdriver.Chrome(DRIVER_PATH)
			driver.get(json_selector("FT_WALTON_PRINTER")) 
			add = driver.find_element_by_xpath(printer2_add_button)
			add.click()
			idx = 0
			for user in (names):
				address_name = driver.find_element_by_xpath(printer2_address_name_button)
				address_name.click()
				address_name.send_keys(user)
				printer_email = driver.find_element_by_xpath(printer2_printer_email_button)
				printer_email.click()
				printer_email.send_keys(user_emails[idx])
				submit = driver.find_element_by_xpath(printer2_register_next_button)
				submit.click()
				idx += 1
			print("Completed Successfully")
			break	

		
		

while True:
	try:
		ask_user_printer = (int(input((" (1) Huntsman Cancer Printer \n (2) Lone Peak Printer \n (3) Mercy SW Printer \n (4) SGHNC Printer \n (5) Maui Coast Printer \n (6) Worthington Tower Printer \n (7) Caesars Printer \n (8) St Marks Printer \n (9) Bayonet Printer \n (10) Hub 202 Printer \n (11) Penske Printer \n (12) Aligned Printer \n (13) Fort Walton Printer \n Enter Selcetion Here: "))))
		if ask_user_printer in range (1, 14):
			jobsite_printer_selection()
		elif ask_user_printer not in (1, 14):
				print("Invalid Input!")
				continue
	except ValueError as err:
		print("Invalid Input!".format(err))

