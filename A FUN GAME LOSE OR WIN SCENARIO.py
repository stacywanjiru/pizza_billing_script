#A FUN GAME LOSE OR WIN SCENARIO
# I WILL ONLY USE THE PAYTHON CONDITION TO TEST ON MY GAME
print(" lets play a game all together\n follow the steps carefull not to be kicked out GOODLUCK")

#decide if you wanna play the game
play_game =input("do you want to play yes or no chose!? >  ")
# tagging along
if play_game == "yes":
    print("get ready")
else:
    print("exit the platform")

coin = input("choose a side of the coin heads or tail ?  ")
if coin == "heads":
    print("sorry your out hehe!!")
else:
    activity = input("do you want to swim or walk choose ONE! ")
    if activity == "swim":
        print("congratulation on reaching this stage")
    elif activity != "swim":
        print("sorry you were so close\n you loooose!!")
#nesting the condition is a super way of having a varaiaty of choices withing your code
    if activity == "swim":
        print("WINNER!!")