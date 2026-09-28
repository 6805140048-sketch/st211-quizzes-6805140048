class Shopping:
    item = "apple"
    apple_price = 20
    amount = int(input("How many apples do you want to buy? "))

    if  amount >= 2:
        apples_price = amount*apple_price
        print("you purchased", amount, "apples")
    elif amount == 1:
        print("you purchased 1 apple")

    item = "banana"
    banana_price = 8
    amount = int(input("How many bananas do you want to buy? "))
    
    if  amount >= 2:
            bananas_price = amount*banana_price
            print("you purchased", amount, "bananas")
    elif amount == 1:
            print("you purchased 1 banana") 
    total_price = apples_price + apple_price + bananas_price + banana_price      
    print ("Your total price is", total_price)  