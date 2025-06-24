secret_no=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess: "))
    if guess==secret_no:
        print("You Win!!")
        break
    else:
        print("Sorry! You failed")
    guess+=1