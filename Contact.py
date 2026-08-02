contact={}

while True:
    print("====Welcome to Akshat App=====")
    print("1, To add contact ")
    print("2,To view all contact")
    print("3,search for contact by name")
    print("4,Delete Contact")
    print("5, Exit")

    choice=input("Enter your choice : ")

    if choice == '1':
        add_name=input("Enter a name")
        add_number=int(input("Enter a contact number : "))

        contact[add_name]=add_number
        print("sucessfully added")

    elif choice == '2':
        print(contact)   

    elif choice == '3':
        name=input("Enter a name you want to search: ")
        if name in contact:
            print(f"{name} contact number ={contact[name]}")
        
        else:
            print(f"{name} was not found in contact")
    elif choice == '4':
        name=input("Enter a name you want to delete : ")   

        if name in contact:
            del contact[name]
            print(f"{name} was sucessfully deleted ")
        else:
            print(f"{name} was not in the contact")
    elif choice == '5':
        print("you have exited") 
        break

                