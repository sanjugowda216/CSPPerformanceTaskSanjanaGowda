# The Purpose of my program is for users to order lemonade from a lemonade stand.
# My program lets a user customize their lemonade order

print("What a beautiful and sunny day! \nWelcomg to Sanjana's Lemonade Stand!\n-----------")
name = input("What is your name: ")

def order():
    flavors = ['original','strawberry','peach','rasberry']
    for i in flavors:
        print(flavors.index(i)+1,i)

order()