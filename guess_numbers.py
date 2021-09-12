import random

def user_guess(x,y):
    random_guess=random.randint(x,y)
    guess=0
    count=0
    while guess!=random_guess:
        guess=int(input(f"choose a no. between {x} and {y}\n"))
        if guess<random_guess:
            print("too low ,guess again")
        elif guess>random_guess:
            print("too high, guess again")
        count+=1
    print(f"congrats you have guessed correctly in {count} attempt ,the no. is {guess}")


def computer_guess(x,y):
    low=x
    high=y
    feedback=""
    count=0
    while feedback!="c":
        if high!=low:
            random_guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f"computer guess is {random_guess},it is high(h) or low(l) or correct(c)\n")
        if feedback=="h":
            high=random_guess-1
        elif feedback=="l":
            low=random_guess+1
        count+=1
    print(f"congrats computer has guessed your no. {random_guess} correctly in {count} attempt")

choice=int(input("choose 1 for user_guess and 2 for computer_guess\n"))
if choice==1:
    low,high=input("choose two no. in which you wanna guess\n").split()
    user_guess(int(low),int(high))
elif choice==2:
    low,high =input("choose two no. in which you wanna guess\n").split()
    computer_guess(int(low),int(high))
else:
    print("invalid input")

