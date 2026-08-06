num = int(input("Enter your number : "))
name = input("Enter your name : ")
contact = {}

contact[name] = num

with open("ContactBook.txt", "a") as f:
    f.write(f"{name} : {num}\n")

print("Contact is successfully added")

print("---- All saved contact------- ")

with open("Contacts.txt","r") as f:
    data=f.read()
    print(data)