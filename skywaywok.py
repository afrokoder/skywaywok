#
# Order Entry program that reduces wait time at a restaurant
#
import time
import datetime


def lunch_time():

    print("Hello and welcome to SkyWay Wok!")
    time.sleep(1)
    print("Today's date and time: ", datetime.datetime.now())
    time.sleep(1)
    print("\n")
    print("Here's a list of Today's Menu!")
    print("Fried Rice, White Rice, Spicy Noodles, Sesame Chicken, Spicy Wings, Stir Fry")
    order = input('would you like One, Two, or Three entrees?')

#
# The User is given a choice of one two or three entrees
#
    if str(order.lower()) == "one":
        one_entree()
    elif str(order.lower()) == "two":
        two_entree()
    elif str(order.lower()) == "three":
        three_entree()
    else:
        print("\n", order, " is not a valid selection")
#
#  The User inputs their selection
#


def one_entree():
    time.sleep(2)
    mon_menu = ["Fried Rice", "White Rice", "Spicy Noodles", "Sesame Chicken", "Spicy Wings", "Stir Fry"]
    print("Select your Item")
    choice1 = input()

    if str(choice1.lower()) == "fried rice":
            print('One Order of Fried Rice Has Been Entered; Please proceed to Cashier')
    elif str(choice1.lower()) == "White Rice":
            print('One Order of White Rice Has Been Entered; Please proceed to Cashier')
    elif str(mon_menu) == "Spicy Noodles":
            print('One Order of Spicy Noodles Has Been Entered; Please proceed to Cashier')
    elif str(mon_menu) == "Sesame Chicken":
            print('One Order of Sesame Chicken Has Been Entered; Please proceed to Cashier')
    else:
            print("Please Select an item from the list")


def two_entree():
    time.sleep(1)
    #mon_menu = ["Fried Rice", "White Rice", "Spicy Noodles", "Sesame Chicken", "Spicy Wings", "Stir Fry"]
    choice1 = input("Please Select your First Item")
    choice2 = input("Please Select your second Item")
    print("Your Order of " + choice1 + " and " + choice2 + " Has been entered")


def three_entree():
    choice1 = input("Please Select your First Item")
    choice2 = input("Please Select your second Item")
    choice3 = input("Please Select your third item")
    print("Your Order of " + choice1 + ", " + choice2 + " and " + choice3 + " Has been entered")
    print("Please proceed to cashier for payment")


print(lunch_time())
