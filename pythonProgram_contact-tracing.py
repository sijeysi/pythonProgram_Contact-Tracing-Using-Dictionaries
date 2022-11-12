print("\n")
print("PROGRAMMED BY: Crystal Jane Cadimas")
print("Course/Year:   BSCOE 2-2")

contact_tracing = {}

# Display a menu option 
print()
print("================ MENU LIST ================\n")
print(" What do you want to do?\n")
print(" [1] Add a contact")
print(" [2] Change a contact")
print(" [3] Search a contact")
print(" [4] Delete a contact")
print(" [5] Delete all contacts")
print(" [6] Display contact's length")
print(" [7] Exit program\n")

# Allow the user to select an item in the menu (check if valid)
selected = int((input("Choose an option: ")))

# Perform the selected option
if selected in (1,2,3,4,5,6,7):
    if selected == 1:
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

        print("\nPLEASE CHECK YOUR PERSONAL DETAILS:")
        print("\n\nFull Name:", fullName,
            "\nAge:", age,
            "\nAddress:", address,
            "\nContact Number:", contactNum,
            "\nBody Temperature:", bodyTemp)

    

else: 
    print("Invalid attempt!")


# Oprion 1: Ask personal data for contact tracing to store the info
# Option 2: Search, ask full name then display the record
# Option 3: Ask the user if s/he wants to exit or retry