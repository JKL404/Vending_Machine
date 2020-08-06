#Python program for vending machine by using data types, operator and control statements___2048014
print ("*******  Welcome to the || 2048014 Vending Machine || *******")
# Asking the Customer how much money they wish to pay.
cash = int(input("Please Input your cash Amount: "))
#checking positve amounts
while cash <= 0:
    cash = int(input("Please enter a correct amount Details: "))
# Displaying the user how much they have entered in total.
print ("\nIn total you have entered Rs", cash)
# Creating variables for the 5 products and their respective prices. 
product_1, product_1_price = "Snickers",50
product_2, product_2_price = "Cookies",120
product_3, product_3_price = "Oreos",40
product_4, product_4_price = "Peanuts",60
product_5, product_5_price = "Coke",30
# Creating variables to track the number of each items bought by the customer,
snickers = 0
cookies = 0
oreos = 0
peanuts = 0
coke = 0

# Displaying Customer of the choices available and the prices .
print ("__________________________________________________________\n")
print ("++++++ There are 5 products available to pick from; ++++++\n")
print ("----------------------------------------------------------\n")
print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))

# Asking the Customer to make a selection of the product.
while cash > 0:
    print ("=====================================================\n")
    choice = input("What would you like to buy? Type N when you are finished \n")
    if choice == "snickers" or choice == "Snickers" and cash >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        if product_1_price < cash:
          cash = round((cash - product_1_price),2)
          snickers = (snickers + 1)
        else:
          print("You donot have enough credits to buy", product_1)
        print ("You have this much money remaining: Rs", cash)
    elif choice == "cookies" or choice == "Cookies" and cash >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        if product_2_price < cash:
          cash = round((cash - product_2_price),2)
          cookies = (cookies + 1)
        else:
          print("You donot have enough credits to buy", product_2)
        print ("You have this much money remaining: Rs", cash)
    elif choice == "Oreos" or choice == "oreos" and cash >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        if product_3_price < cash:
          cash = round((cash - product_3_price),2)
          oreos = (oreos + 1)
        else:
          print("You donot have enough credits to buy", product_3)
        print ("You have this much money remaining: Rs", cash)
    elif choice == "Peanuts" or choice == "peanuts" and cash >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        if product_4_price < cash:
          cash = round((cash - product_4_price),2)
          peanuts = (peanuts + 1)
        else:
          print("You donot have enough credits to buy", product_4)
        print ("You have this much money remaining: Rs", cash)
    elif choice == "Coke" or choice == "coke" and cash >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        if product_5_price < cash:
          cash = round((cash - product_5_price),2)
          coke = (coke + 1)
        else:
          print("You donot have enough credits to buy", product_5)
        print ("You have this much money remaining: Rs", cash)
    elif choice == "N" or choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (product_1, "x", snickers)
        print (product_2, "x", cookies)
        print (product_3, "x", oreos)
        print (product_4, "x", peanuts)
        print (product_5, "x", coke)
        print ("You have Rs", cash, "remaining.")
        break
    elif cash <= 0:
        print ("???  You have run out of money. ???\n")
        print ("----------------------------------------------------------\n")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print ("----------------------------------------------------------\n")
        print (product_1, "x", snickers)
        print (product_2, "x", cookies)
        print (product_3, "x", oreos)
        print (product_4, "x", peanuts)
        print (product_5, "x", coke)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print ("Thank you for purchasing with us :)\n Please Vist again!")
        break
    else:
        print ("Your choice is wrong or you donot have enough credits!!.")
