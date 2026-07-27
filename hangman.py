import random
words = {
    "python": "A popular programming language",
    "apple": "A common fruit",
    "book": "uses for study purpose",
    "computer": "An electronic device",
    "school": "A place where students learn"
}

word = random.choice(list(words.keys()))
hint = words[word]

guessed_word = ["_"] * len(word)


guessed_letters = []
wrong_guesses = 0
max_wrong = 5

print("=== Welcome to Hangman ===")
print("Hint:", hint)     
while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Wrong Guesses Left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)

    if word == "python":
        print("Hint: Python is a popular programming language.")
    elif word == "apple":
        print("Hint: Apple is a healthy fruit.")
    elif word == "banana":
        print("Hint: Bananas are rich in potassium.")
    elif word == "computer":
        print("Hint: A computer is an electronic device used for computing.")
    elif word == "school":
        print("Hint: School is a place where students learn.")
else:
    print("\n❌ Game Over! The word was:", word)