import random

def hangman():
    word_list = ["python", "programming", "computer", "science", "developer"]
    word = random.choice(word_list)
    guesses = 6
    letters_guessed = []
    word_completion = "_" * len(word)

    while guesses > 0 and word_completion != word:
        print("Guesses remaining:", guesses)
        print("Word:", word_completion)
        guess = input("Guess a letter: ").lower()

        if guess in letters_guessed:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            letters_guessed.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in
 
enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if word_completion == word:
                print("Congratulations! You guessed the word:", word)
        else:
            guesses -= 1
            letters_guessed.append(guess)
            print("Incorrect guess.")
            
    if guesses == 0:
        print("You ran out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()