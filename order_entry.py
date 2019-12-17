import time
import datetime
from datetime import date 

#Welcome Screen 
print("Hello and welcome to SkyWay Wok!")
time.sleep(1)
print("\n\n")

print("Today's date and time: ", datetime.datetime.now())
time.sleep(1)


#Display list of available items
menu = ["bread","toast","eggs","muffins"]
print ("Todays Menu: ", *menu, sep = "\n")

#List that holds the items being ordered by the customer 
ordered = []

#defining the order entry process

def entree(): 
    for item in range(0,5): #allows up to x amount of orders to be placed 
         
        item = input('enter your item: press q to quit: ') #takes in the customers order or Q to quit
        item = item.lower()
        #while item != 'q':
        if item == "q":
            break

        if item in menu: 
            print(f"your order of {item} has been placed") 
            ordered.append(item)

        elif item == '':
            print("please enter a valid item")

        else: 
            print("please try again")
            break 
    return(ordered)                                     
        
entree()
 
print('your order of', ordered, 'has been placed')
