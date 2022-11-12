# ---------------- CONTEXT -----------------
#  Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				    Use dictionary to store the info
# 				    Use the full name as key
# 				    The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"

database = {}

#usrDecision = "proceed"  # Loop counter variable 

usrFName = input("Full Name: ") # Prompts for personal details --- OPTION 1
usrAge = input("Age: ")
usrAddr = input("Address: ")
usrCNum = input("Contact No.: ")

queryProf = dict({
    "Full Name": usrFName,
    "Age": usrAge,
    "Address": usrAddr,
    "Contact No.": usrCNum
})

print(type(queryProf))
print(queryProf)

# while usrDecision == "proceed": # Main Loop
#     print("What would you like to do?\n\nMenu:\n\nType "1" to register a profile.\nType "2" to search a profile.\nType "3" or "exit" to terminate.")
#     usrAction = input("> ")
# else:
#     print("Have a nice day! :)")
