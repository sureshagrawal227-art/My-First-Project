def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def expo(a,b):
    return a**b
def div(a,b):
    if b==0:
        return "invalid value"
    return a/b 

while True:
    print("===Python calculator===")
    print("1,Addition (+)")
    print("2,Subtraction (-)")
    print("3,multiply (*)")
    print("4,division (/)")
    print("5,expontential (**)")
    print("===Exit===")

    choice=input("Enter of your choice(1-5): ")

    if choice in ("1","2","3","4","5"):
        try:
            num1=float(input("Enter your first number : "))
            num2=float(input("Enter your second number:"))
        except ValueError:
            print("invalid")
            continue
        if choice =='1':
             
             print(f"result:{num1}+{num2}={add(num1,num2)}")
        elif choice =='2':
            print(f"Result:{num1}-{num2}={sub(num1,num2)}")
        elif choice =='3':
            print(f"Result:{num1}*{num2}={mult(num1,num2)}")     
        elif choice =='4':
            print(f"Result:{num1}/{num2}={div(num1,num2)}")   
        elif choice =='5':
            print(f"Result:{num1}**{num2}={expo(num1,num2)}")   

        else:
         print("invalid choice")   


  
    

