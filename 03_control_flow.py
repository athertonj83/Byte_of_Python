#control flow


print("\n\n*** If conditions ***")
number=23
guess=int(input("Enter an integer:")) #input functions return input as a string which is why we convert to int

if guess==number:
    print("Congrats, you guessed it!")
    print('(but you do not win a prize!)')
elif guess<number:
    print("Nope, higher than that")
else:
    print("Nope, lower than that")
print("Done")




print("\n\n*** While conditions ***")
number=23
running=True

while running:
    guess=int(input("Enter an integer:"))

    if guess==number:
        print("Congrats, you guessed it!")
        running=False
    elif guess<number:
        print("Nope, higher than that")
    else:
        print("Nope, lower than that")
else: #once while is done, else always executed unless there is a break statement
    print("The while loop is over")
print("Done")


print("\n\n*** For loops ***")
