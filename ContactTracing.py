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

def removeSpaces(strn):
    if len(strn.split()) >= 2:
        splits = strn.split()
        for i in splits:
            i.capitalize()
        checkspaces = " ".join(splits)
        return checkspaces
    else:
        finalstr = strn.replace(" ", "")
        return finalstr

Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
BBlue = "\u001b[34;1m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"
DCyan = "\u001b[36;1m"
Cyan = "\u001b[36"

database = {}

usrDecision = "proceed"  # Main Loop counter variable 

while usrDecision == "proceed": # Main Loop
    print("\nWhat would you like to do?\n\nMenu:\n\nType '1' to register a profile.\nType '2' to search a profile.\nType '3' or 'exit' to terminate.")
    usrAction = input("\n> ")
    if usrAction == "1": 
        print("\nProvide your personal details below.\n")
        print("Full Name")    # Prompts for personal details --- OPTION 1
        usrFName = removeSpaces(input("  First Name : "))
        usrMName = removeSpaces(input("  Middle Name: "))
        usrLName = removeSpaces(input("  Last Name  : "))
        usrAge =   input("\nAge         : ")
        usrAddr =  input("Address     : ")
        usrCNum =  input("Contact No. : ")
        print("\nVerify your details", "\nDo you want to confirm this profile? (Y/N)")
    
        queryProf = dict({
            "Full Name": [usrFName, usrMName, usrLName],
            "Age": usrAge,
            "Address": usrAddr,
            "Contact No.": usrCNum
        })

        for label, details in queryProf.items():
            if label == "Full Name":
                ConcatinatedName = ""
                for namefragment in details:
                    ConcatinatedName += namefragment + " "
                print(label, "  :", ConcatinatedName)
            elif label == "Age":
                print(label, "        :", details)
            elif label == "Address":
                print(label, "    :", details)
            elif label == "Contact No.":
                print(label, ":", details)
    
        usrVerify = input("\n> ").lower()
        
        while True:
            if usrVerify == "y":
                database_items = len(database)
                database.update({f"Data {database_items+1}": queryProf})
                print("Profile Saved!")
                break
            elif usrVerify == "n":
                print("Are you sure you want to discard this profile? (Y/N)")
                while True:
                    usrDiscard = input("\n> ").lower()
                    if usrDiscard == "y":
                        break
                    elif usrDiscard == "n":
                        database_items = len(database)
                        database.update({f"Data {database_items+1}": queryProf})
                        print("Profile Saved!")
                        break
                    else:
                        print("Enter a valid command")
                break
            else:
                print("Enter a valid command")

    elif usrAction == "2":
        usrSearchFilter1 = removeSpaces(input("Enter First Name: "))
        usrSearchFilter2 = input("Enter Middle Name: ")
        usrSearchFilter3 = input("Enter Last Name: ")
        break
    elif (usrAction == "3") or (usrAction == "exit"):
        usrDecision = "terminate"
else:
    print("Have a nice day! :)")
