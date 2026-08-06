contact={}

while True:
    print("====Welcome to Akshat App=====")
    print("1, To add contact ")
    print("2, To view all contact")
    print("3, search for contact by name")
    print("4, Delete Contact")
    print("5, Exit")

    choice=input("Enter your choice : ")

    if choice == '1':
        add_name=input("Enter a name: ")
        add_number=int(input("Enter a contact number : "))

        contact[add_name]=add_number
        with open("ContactBook.txt","a") as f:
            f.write(f"{add_name}: {add_number}\n")
        print("sucessfully added")

    elif choice == '2':
        with open("ContactBook.txt","r") as f:
            data=f.read()
            print(data)  

    elif choice == '3':

        name=input("Enter a name you want to search: ")
        with open("ContactBook.txt","r") as f:
            for line in f:
                if name in line:
                    print(line.strip())
                    found=True
                if not found:
                     print(f"{name} was not found in contact")
    elif choice == '4':
        name=input("Enter a name you want to delete : ")  
        deleted=False
        with open("ContactBook.txt","r") as f:
            lines=f.readlines()
        with open("ContactBook.txt","w") as f:
          
            for line in lines:
                if name in line:
                    deleted=True
                else:
                    f.write(line)
        if deleted:
            print(f"{name} was sucessfully deleted")
        else:
            print(f"{name} was not found")                     

    elif choice == '5':
        print("you have exited") 
        break

                