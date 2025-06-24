word=input(" ").lower()
while word=="help":
    print("start -> to start the car")
    print("stop -> to stop the car")
    print("quit -> to exit")
    entered_word=input("what do you want to do? ").lower()
    if entered_word=="start":
        print("Car started...Ready to go!")
        
    elif entered_word=="stop":
        print("Car stopped.")
    elif entered_word=="quit":
        print("You have succesfully exited the game")
        break
    else:
        print("I don't understand that...")
    