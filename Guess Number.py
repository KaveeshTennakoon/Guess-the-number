import random

def guess():
    num=random.randint(1,100)
    flag=False
    count=0
    guessed=int(input("Enter your guess: "))
    while flag==False:
        if num == guessed:
            flag=True
        elif guessed<num:
            guessed=int(input("Guess is lower, try again: "))
        elif guessed>num:
            guessed=int(input("Guess is higher, try again: "))
        count=count+1
    return count

attempt=guess()
print()
print("You took",attempt,"attempts")
if attempt<5:
    print("Excellent! You guess in fewer than 5 guesses")
else:
    print("Try to guess with less attempts, Better luck next time")
