print("\n")
print("PROGRAMMED BY: Crystal Jane Cadimas")
print("Course/Year:   BSCOE 2-2")

contact_tracing= {}
contact_tracing1 = {}
contact_tracing2 = {}

# Display a menu option 
def main():                     
    def menuList():
        print()
        print("================ MENU LIST ================")
        print(" \nWhat do you want to do?")
        print(" [1] Add a contact")
        print(" [2] Modify a contact")
        print(" [3] Delete a contact")
        print(" [4] Delete all contacts")
        print(" [5] Display contact list")
        print(" [6] Exit program\n")
    menuList()
    # Allow the user to select an item in the menu (check if valid)
    selected = int((input("Choose an option: ")))

    # Perform the selected option
    if selected in (1,2,3,4,5,6,7):
        if selected == 1:
            def addContact():
                print("\n\n============== ADD CONTACT ===============")
                fullName = input("\nEnter your full name: ")
                age = input("Enter your age: ")
                address = input("Enter your complete address: ")
                contactNum = int(input("Enter your active contact number: "))
                bodyTemp = int(input("Enter your body temperature: "))

                contact_tracing["Full Name"] = fullName
                contact_tracing["Age"] = age
                contact_tracing["Address"] = address
                contact_tracing["Contact Number"] = contactNum
                contact_tracing["Body Temprature"] = bodyTemp

                print("\n\nPLEASE CHECK YOUR PERSONAL DETAILS:")
                print("Full Name:", fullName,
                    "\nAge:", age,
                    "\nAddress:", address,
                    "\nContact Number:", contactNum,
                    "\nBody Temperature:", bodyTemp)
                print("\n",contact_tracing)

                repeat = input("\n\nWould you like to continue, yes or no? ")
                if repeat.lower() == "yes":
                    main()
                elif repeat.lower() == "no":
                    print("\n\nThank you for using this program!")
                    print("Have a nice day :)")
                    exit()
                else:
                    print("\nInvalid input! Please try again!")
                    main()     
            addContact()

        elif selected == 2:
            def modifyContact():
                print("\n\n============== MODIFY A CONTACT ===============")

                print(" \nWhat do you want to modify?")
                print(" [a] Full Name")
                print(" [b] Age")
                print(" [c] Address")
                print(" [d] Contact Number")
                print(" [e] Body Temperature")

                change_contact = input(" \nChoose an option: ")

                if change_contact in ("a","b","c","d","e"):
                    print()
                    print(contact_tracing, "\n\n")
                    if change_contact == "a":
                        newName = input("Enter new name: ")
                        contact_tracing["Full Name"] = newName
                        print("Modifed name:", newName)
                        print()
                        print(contact_tracing)

                    elif change_contact == "b":
                        newAge = input("Enter new age: ")
                        contact_tracing["Age"] = newAge
                        print("Modifed age:", newAge)
                        print()
                        print(contact_tracing)

                    elif change_contact == "c":
                        newAddress = input("Enter new address: ")
                        contact_tracing["Address"] = newAddress
                        print("Modifed address:", newAddress)
                        print()
                        print(contact_tracing)

                    elif change_contact == "d":
                        newContactNum = input("Enter new active contact number: ")
                        contact_tracing["Contact Number"] = newContactNum
                        print("Modifed contact number:", newContactNum)
                        print()
                        print(contact_tracing)

                    elif change_contact == "e":
                        newBodyTemp = input("Enter new body temperature: ")
                        contact_tracing["Body Temperature"] = newBodyTemp
                        print("Modifed body temperature:", newBodyTemp)
                        print()
                        print(contact_tracing)

                    repeat = input("\n\nWould you like to continue, yes or no? ")
                    if repeat.lower() == "yes":
                        main()
                    elif repeat.lower() == "no":
                        print("\n\nThank you for using this program!")
                        print("Have a nice day :)")
                        exit()
                    else:
                        print("\nInvalid input! Please try again!")
                        main()
            modifyContact()

main()