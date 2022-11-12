print("\n")
print("PROGRAMMED BY: Crystal Jane Cadimas")
print("Course/Year:   BSCOE 2-2")

contact_tracing = {}

# Display a menu option 
def main():                     
    def menuList():
        print()
        print("================ MENU LIST ================")
        print(" \nWhat do you want to do?")
        print(" [1] Add a contact")
        print(" [2] Modify a contact")
        print(" [3] Search a contact")
        print(" [4] Delete a contact")
        print(" [5] Delete all contacts")
        print(" [6] Display contact's length")
        print(" [7] Exit program\n")
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

                contact_tracing[fullName] = fullName
                contact_tracing[age] = age
                contact_tracing[address] = address
                contact_tracing[contactNum] = contactNum
                contact_tracing[bodyTemp] = bodyTemp 

                print("\n\nPLEASE CHECK YOUR PERSONAL DETAILS:")
                print("\nFull Name:", fullName,
                        "\nAge:", age,
                        "\nAddress:", address,
                        "\nContact Number:", contactNum,
                        "\nBody Temperature:", bodyTemp, "degree")
            addContact()

        elif selected == 2:
            def modifyContact():
                print("\n\n============== MODIFY A CONTACT ===============")

                print(" \nWhat would you like to modify?")
                print(" [2.1] Full Name")
                print(" [2.2] Age")
                print(" [2.3] Address")
                print(" [2.4] Contact Number")
                print(" [2.5] Body Temperature")

                change_contact = input(" \nChoose an option: ")

                if change_contact in (2.1,2.2,2.3,2.4,2.5):
                    if change_contact == 2.1:
                         print("hello")
            modifyContact()

main()