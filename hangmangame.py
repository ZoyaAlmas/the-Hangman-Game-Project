import random
import hangmanstages
class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.guessed_letters = []
        self.attempts = 6

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def play(self):
        print("Welcome to Hangman Game!")
        print(self.display_word())

        while self.attempts > 0:
            guess = input("Guess a letter: ").lower()

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
            elif guess in self.word:
                self.guessed_letters.append(guess)
                print(self.display_word())
                if "_" not in self.display_word():
                    print("Congratulations! You guessed the word:", self.word)
                    break
            else:
                self.guessed_letters.append(guess)
                self.attempts -= 1
                print("Incorrect! You have", self.attempts, "attempts left.")
                print(self.display_word())
                print(hangmanstages.stages[self.attempts])

        if self.attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", self.word)

# Example usage:
word_list = ["apple", "banana", "orange", "grapes", "pear", "strawberry", "blueberry", "chair", "tomato", "sofa",
             "bed", "dinningtable", "capsicum", "rohan", "hospital", "mumbai", "lucknow", "chennai", "lemon"]
game = Hangman(word_list)
game.play()
