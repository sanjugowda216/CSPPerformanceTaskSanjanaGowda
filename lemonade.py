# The Purpose of my program is for users to order lemonade from a lemonade stand.
# My program lets a user customize their lemonade order

print("What a beautiful and sunny day! \nWelcome to The Lemonade Stand!\n------------------------------")
name = input("What is your name: ")

#name and parameter
def order(name):
    flavors = ['original','strawberry','peach','rasberry'] #list of flavor options
    flavorOrder = ''
    
    #printing a visual of the menu options
    for i in flavors:
        print(flavors.index(i)+1,i)

    print("\nHello "+ name +"! What would you like to order?") 
    myFlavor = input("Please enter a number from 1-4: ")
    
    #order response checking if input is a digit
    while myFlavor not in ["1","2","3","4"]:
        myFlavor = input("Invalid input. Please select a menu number from 1-4: ")
        
    if myFlavor == "1":
        print("\nYou ordered an "+flavors[0]+" lemonade!")
        flavorOrder = flavors[0]
    elif myFlavor == "2":
        print("\nYou ordered a "+flavors[1]+" lemonade!")
        flavorOrder = flavors[1]
    elif myFlavor == "3":
        print("\nYou ordered a "+flavors[2]+" lemonade!")
        flavorOrder = flavors[2]
    elif myFlavor == "4":
        print("\nYou ordered a "+flavors[3]+" lemonade!")
        flavorOrder = flavors[3]
    
    # lemon customizing and message returning option
    print("\n\nHow many freshly squeezed lemons would you like in your "+flavorOrder+" lemonade ?")
    lemons = input("Choose a number from 1-10: ")

    while not lemons.isdigit() or int(lemons)<1 or int(lemons)>10:
        lemons = input("Invalid input: Please select the number of lemons from 1-10: ")
    lemons = int(lemons)
    #uses comparing operators
    if int(lemons) <= 3:
        print("\nThat sounds perfect! Your "+flavorOrder+" lemonade with  "+ str(lemons)+" lemons is on its way.\n\nHave a great day "+name+"!")
    elif lemons <=6:
        print("\nOooh interesting selection, you are feeling a little sour today. Your " + flavorOrder + " lemonade with " +str(lemons) + " lemons is right up!\n\nEnjoy the rest of your day "+name+"!")
    elif lemons <= 10:
        print("\nWOW you are SOUR! When life gives you lemons, you seem to make the most of them! Your "+ flavorOrder +" lemonade with " +str(lemons)+" lemons is coming right up!\n\nEnjoy your sunny day " +name + "!") 
  

#call to student developed procedure 
order(name)