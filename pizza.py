print("WELCOME TO MAMA NICE PIZZA PALACE ")
print("YOUR FAVARITE GO TO PIZZA JOINT ")
pizza_size=input(" what size of pizza do you want to order small, medium, or large? >>").lower()
pepperoni=input("do you want pepporoni added on your pizza yes or no? >>").lower()
extra_cheese=input("do you want etra cheese on your pizza yes or no? >>").lower()

#calculate the bill of the pizza

#depending on customers pizza size

bill = 0
if pizza_size == "small":
    bill +=20
elif pizza_size == "medium":
    bill =30    
elif pizza_size == "large":
    bill =50
else:
    print("wrong inpute of choice try again!!!")
#depending on the choice of pepperoni

if pepperoni == "yes":
    bill +=10
else:
    print("make your order again")
#depending on the choice of pepperoni

if extra_cheese == "yes":
    bill +=5
else:
    print("check your order again")
print(f"your total bill is:{bill}")

