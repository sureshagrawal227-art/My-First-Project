Stocks=int(input("How many rupees stocks you have invested till now ? :"))
data=input("Did you make profit or loss ? :")

if data=="profit":
    profit=int(input("How much profit you made? :"))
    total=Stocks+profit
    print(f"You made good work having {total} rupees on your hand , all the best for future ")
    print("=======================================")
    print("=======================================")


elif data=="loss":
    loss=int(input("How much loss you have get? :"))
    total=Stocks-loss
    print(f"You made {total} ruppes , which is not good try harder next time ")
    print("=======================================")

else:
    print("Invalid Response, please write a valid response")
    print("thank you ")
    print("=======================================")

    

