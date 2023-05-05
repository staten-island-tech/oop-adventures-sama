import random

class Hangman:
    hangman = (r'''
____
|/   |
|   
|    
|    
|    
|
|_____ ''', r'''
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____''', r'''
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____''', r'''
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____''', r'''
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____''', r'''
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____ ''')

def __init__(self, word):
    self.word = word
    self.letters = ''
    
def play():  
    words = ["quokka", "ferret", "hedgehog"]
    attempts = 5
    hangman = Hangman(random.choice(words))
    for attempt in range(1, attempts + 1):
        if result == "win":
            break
        print("{0} attempts remain".format(attempt))
    print("The word is " + hangman.word)
    print("Goodbye.")

        

def ask_letter(self):
        while True:
            letter = input("Guess a letter: ")
            if letter in self.letters:
                print("This letter is already played, sorry")
                continue
        