low = 0
high = 100
answer = (high + low)/2
print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")
test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 
while test != "c":
    if test != "h" and test != "l" and test != "c":
        print ("Sorry, I did not understand your input.")
    elif test == "h":
        high = answer
    elif test == "l":
        low = answer
    else:
        break
    answer = int((high + low)/2)
    print("Is your secret number " + str(int(answer)) +"?")
    test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 
print("Game over. Your secret number was: " + str(int(answer)))

    