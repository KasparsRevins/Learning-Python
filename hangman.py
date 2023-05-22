def hangman(word):
    word = word.lower() 
    word_length = len(word)
    guessed_letters = ["_"] * word_length  
    incorrect_guesses = 0
    max_incorrect_guesses = 7  

    print("_ " * word_length)

    while True:
        if incorrect_guesses == max_incorrect_guesses:
            print("Too many mistakes. You lost!")
            break

        guess = input("Enter your guess: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_letters[i] = guess
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

        print(" ".join(guessed_letters))

        if "_" not in guessed_letters:
            print("Congratulations! You guessed the word correctly.")
            break

hangman("hangman")