from officeprinteradder import office_printer_adder
from jobsiteprinteradder import jobsite_printer_selection

if __name__ == '__main__':
	# Asks user if jobsite or office printer (Main selection)
	while True:
		try:
			ask_type = (int(input("What kind of printer is this? \n(1) Office Printer \n(2) Jobsite Printer \nEnter answer here:")))
			if ask_type == 1:
				office_printer_adder()
			elif ask_type == 2:
				jobsite_printer_selection()
			elif ask_type not in (1, 2):
				print("Invalid Input!")
				continue
		except ValueError as err:
			print("Invalid Input: {}".format(err))
