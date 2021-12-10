def hangman(secret_word):

    '''

    secret_word: string, the secret word to guess.


    Hangman game yeh start karta hai:


    * Game ki shuruaat mei hi, user ko bata dete hai ki

      secret_word mei kitne letters hai


    * Har round mei user se ek letter guess karne ko bolte hai


    * Har guess ke baad user ko feedback do ki woh guess uss

      word mei hai ya nahi


    * Har round ke baar, user ko uska guess kiya hua partial word

      display karo, aur underscore use kar kar woh letters bhi dikhao

      jo user ne abhi tak guess nahi kiye hai
    '''
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("")
    letters_guessed = []
    while (True):
        available_letters = available_letters(letters_guessed)
        print("Available letters: " + available_letters)
        guess =input("Please guess a letter: ")
        letter = guess.lower()
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: " + guess(secret_word, letters_guessed))
            print ("")
            if letters_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            letters_guessed.append(letter)
            print ("Oops! That letter is not in my word: " + letters_guessed(secret_word, letters_guessed)
            # letters_guessed.append(letter)
            # print ("")
