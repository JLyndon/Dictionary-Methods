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
        return finalstr.capitalize()

Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
BBlue = "\u001b[34;1m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"

print("\n",f"Contact Tracing \33[41m{Bldtxt} Dictionary Methods {End}!".center(71, " "), "\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "),"\n", f"Feel free to {Red}explore{End} the program {Grn}features{End}!".center(77, " "), "\n", f"Register your profile; Stay {Blue}Safe{End} and {Yllw}Connected{End}.".center(80, " "),"\n","\n",f"{Blue}{Itlc}\nChoose an action from the menu{End}:")

database = {}

usrDecision = "proceed"  # Main Loop counter variable 

while usrDecision == "proceed": # Main Loop
    print("\nWhat would you like to do?\n\n", f"\n\33[44m{Bldtxt}       Menu       {End}", f"\n\n   Type '{Grn}1\33[0m' to register a profile.\n   Type '{Blue}2\33[0m' to search for a profile.\n   Type '{Red}3\33[0m' or '{Red}exit\33[0m' to terminate the program.")
    choices = ["1","2","3","exit"]
    usrAction = ""
    while True:
        decisionU = input("\n> ").lower()
        if decisionU in choices:
            usrAction = decisionU
            break
        else:
            print(f"{Red}Enter a valid command{End}")
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
                nameConcat = " ".join(queryProf["Full Name"]) 
                database.update({nameConcat : queryProf})
                print(f"{Grn}\nProfile Saved!{End}")
                break
            elif usrVerify == "n":
                print("Are you sure you want to discard this profile? (Y/N)")
                while True:
                    usrDiscard = input("\n> ").lower()
                    if usrDiscard == "y":
                        break
                    elif usrDiscard == "n":
                        database_items = len(database)
                        nameConcat = " ".join(queryProf["Full Name"]) 
                        database.update({nameConcat : queryProf})
                        print(f"{Grn}\nProfile Saved!{End}")
                        break
                    else:
                        print(f"{Red}Enter a valid command{End}")
                break

    elif usrAction == "2":
        proceeding = "proceed"
        while proceeding == "proceed":
            print("Search by: Full Name")
            usrNameFilter1 = removeSpaces(input("\nEnter First Name: "))
            usrNameFilter2 = removeSpaces(input("Enter Middle Name: "))
            usrNameFilter3 = removeSpaces(input("Enter Last Name: "))
            searchKey = " ".join([usrNameFilter1, usrNameFilter2, usrNameFilter3])
            collectData = []
            for i, j in database.items():
                collectData.append(i)
                if i == searchKey:
                    for key, val in j.items():
                        if key == "Full Name":
                            ConcatinatedName = ""
                            for namefragment in val:
                                ConcatinatedName += namefragment + " "
                            print(key, "  :", ConcatinatedName)
                        elif key == "Age":
                            print(key, "        :", val)
                        elif key == "Address":
                            print(key, "    :", val)
                        elif key == "Contact No.":
                            print(key, ":", val)
            if searchKey not in collectData:
                print(f"{Red}\nSorry, {searchKey} does not exist in our list of contacts.{End}")
            print("\n\nDo you want to proceed to menu? (Y/N)")
            while True:
                usrVery = input("\n> ").lower()
                if usrVery == "y":
                    proceeding = "not"
                    break
                elif usrVery == "n":
                    print("\nDo you want to continue searching? (Y/N)")
                    while True:
                        decideOpt2 = input("\n> ").lower()
                        if decideOpt2 == "y":
                            break
                        elif decideOpt2 == "n":
                            proceeding = "not"
                            break
                        else:
                            print(f"{Red}Enter a valid command{End}")
                    break
                else:
                    print(f"{Red}Enter a valid command{End}")
        
    elif (usrAction == "3") or (usrAction == "exit"):
        usrDecision = "terminate"
    else:
        print(f"\n{Red}Enter a valid command{End}")
else:
    print(f"{Yllw}Have a nice day! :){End}")
