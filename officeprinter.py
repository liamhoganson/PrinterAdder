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
DRIVER_PATH =  ("FILEPATH")

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


# Sandy Office Printers
LCC_ESTCSG_MX3110 = ("ipaddress")
LCC_ESTCCG_MX3140N = ("ipaddress")
LCC_EXEC_MX4141N = ("ipaddress")
LCC_ACCT_MXM904 = ("ipaddress")
LCC_CSG_MX3571 = ("ipaddress")

# Other Office Printers
DENVER_PRINTER = ("ipaddress")
SAN_DIEGO_PRINTER = ("ipaddress")
IRVINE_PRINTER = ("ipaddress")
BRENTWOOD_PRINTER = ("ipaddress")
PHOENIX_PRINTER = ("ipaddress")



# Asks user if jobsite or office printer (Main selection)
while True:
	try:
		ask_type = (int(input("What kind of printer is this? \n(1) Office Printer \n(2) Jobsite Printer \nEnter answer here:")))
		if ask_type == 1:
			break
		elif ask_type == 2:
			break
		elif ask_type not in (1, 2):
			print("Invalid Input!")
			continue
	except ValueError as err:
		print("Invalid Input: {}".format(err))
	

# Office Printer Function

# Grabs list of names from user
def office_printer_adder(printer):

	# Grabs list of names from user and converts to list
	names = []
	print("Enter user's first and last name's on seperate lines. For example: \nFirst name Last name \nFirst name Last name \nEnter answer here:") 
	while True: 
		line = input("") 
		if line == "": 
			break 
		else:
			names.append(line)



# Grabs email based off first and last name from AD
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



# Adds printer selection in bulk
	while printer <= (11):
			try:
				if ask_printer == 1:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(LCC_ESTCSG_MX3110) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break
				
				elif ask_printer == 2:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(LCC_ESTCCG_MX3140N) 
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
				
				elif ask_printer == 3:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(LCC_EXEC_MX4141N) 
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
				
				elif ask_printer == 4:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(LCC_ACCT_MXM904) 
					add = driver.find_element_by_xpath(printer2_add_button)
					add.click()
					idx = 0
					for name in names:
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

				elif ask_printer == 5:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(LCC_CSG_MX3571) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break

				elif ask_printer == 6:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(DENVER_PRINTER) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break

				elif ask_printer == 7:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(SAN_DIEGO_PRINTER) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break

				elif ask_printer == 8:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(IRVINE_PRINTER) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break

					# Not working
				elif ask_printer == 9:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(BRENTWOOD_PRINTER) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break

				elif ask_printer == 10:
					driver = webdriver.Chrome(DRIVER_PATH)
					driver.get(PHOENIX_PRINTER) 
					add = driver.find_element_by_xpath(printer1_add_button)
					add.click()
					idx = 0
					for name in (names):
						address_name = driver.find_element_by_xpath(printer1_address_name_button)
						address_name.click()
						address_name.send_keys(name)
						printer_email = driver.find_element_by_xpath(printer1_printer_email_button)
						printer_email.click()
						printer_email.send_keys(user_emails[idx])
						submit = driver.find_element_by_xpath(printer1_register_next_button)
						submit.click()
						idx += 1
					print("Completed Successfully")
					break
			
			except ValueError as err:
				print("Invalid input {}".format(err))
			except:
				raise ("Could not launch program")
		


if ask_type == 1:
	while True:
		try:
			ask_printer = (int(input(("Which printer would you like to configure? \n (1) LCC_ESTCSG_MX3110 \n (2) LCC_ESTCCG_MX3140N (ICS Printer) \n (3) LCC_EXEC_MX4141N \n (4) LCC_ACCT_MXM904 \n (5) LCC_CSG_MX3571 (9020 Printer) \n (6) Denver Office Printer \n (7) San Diego Printer \n (8) Irvine Printer \n (9) Brentwood Printer \n (10) Phoenix Printer \n Select answer here: "))))
			if ask_printer in range (1, 11):
				office_printer_adder(ask_printer)
			elif ask_printer not in range(1, 11):
				print("Invalid Input!")
				continue
		except ValueError as err:
			print("Invalid Input: {}".format(err))


