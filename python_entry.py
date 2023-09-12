# This is the start of the entry level coding stuff for BIT M1 (CS) done by T. van Beelen and A. Capitano

#1
def hello_world_python():
	print("M1BIT: Hello, Python World!")
#2
def hello_world_one_line():
	print("Hello, world, this is a Python def function.\nIt's awesome to make the computer do stuff!")
#3
def fancy_hello_world():
	print("""
    _    ____   ____ ___ ___ 
   / \  / ___| / ___|_ _|_ _|
  / _ \ \___ \| |    | | | | 
 / ___ \ ___) | |___ | | | | 
/_/   \_\____/ \____|___|___|
""")
#4
def grade_is_valid(grade):
	if 1 >= grade <= 10:
		return True
	else:
		return False
	print(grade_is_valid(grade))
#5
def test_is_valid(test):
	if isinstance(test,int) and (1 >= test <= 3):
		return True
#6
def is_the_same(message1, message2):
	if isinstance(message1, str) and isinstance(message2, str):
		if message1.casefold() == message2.casefold():
			return True
		else: return False
	
	return None
#7
def month_name(month_number):
	if isinstance(month_number, int) and (1 <= month_number <= 12):
		match month_number:
			case "1":
				return "January"
			case "2":
				return "February"
			case "3":
				return "March"
			case "4":
				return "April"
			case "5":
				return "May"
			case "6":
				return "June"
			case "7":
				return "July"
			case "8":
				return "August"
			case "9":
				return "September"
			case "10":
				return "October"
			case "11":
				return "November"
			case "12":
				return "December"
	
	else: print("Invalid argument. The month_number must be an int value between 1 and 12")
#8


print(month_name(2))

