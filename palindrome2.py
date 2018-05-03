def palin(word):
    if len(word) < 1:
        return True
    else:
        if word[0] == word[-1]:
            return palin(word[1:-1])
        else:
            return False
userInput=(input("Enter a single word."))
if(palin(userInput)==True):
    print("Congratulations, this is a palindrome!")
else:
    print("Sorry, try again.")