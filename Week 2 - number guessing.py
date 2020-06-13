feedback = ''
options = ['h','l','c']
low = 0
high = 100
print("Please think of a number between 0 and 100!")

while feedback != 'c':
    avg = (high+low)//2
    print("Is your secret number " + str(avg) + "?")
    feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if feedback not in options:
        print("Sorry, I did not understand your input.")

    elif feedback == 'h':
        high = avg
     
    elif feedback == 'l':
        low = avg
        
if feedback == 'c':
    print("Game over. Your secret number was: ", avg)


