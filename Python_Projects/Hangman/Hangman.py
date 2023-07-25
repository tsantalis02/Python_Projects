import random 
from words import word_list

def randword():
    word = random.choice(word_list)
    return word

def guess(word):
    tries = 6
    guessed = False
    guessedletters = []
    complete_word = "_" * len(word)
    print("Hangman! Let's start!")
    print(complete_word)
    printHangman(tries)
    print()
    while not guessed  and tries > 0:
        guess = input("Guess a letter: ")
        if guess in guessedletters:
            print("You already guessed this letter",guess)
        elif guess not in word:
            print(guess,"not in word. Wrong guess :(")
            tries -= 1
            guessedletters.append(guess)
        else:
            print("Right guess :)",guess,"is in the word!")
            guessedletters.append(guess)
            word_as_list = list(complete_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            complete_word = "".join(word_as_list)
            if "_" not in complete_word:
                guessed = True
            print(complete_word)
            printHangman(tries)
            print()
    if guessed:
      print("Congrats, you guessed the word! You win :)")
    else:
      print("Sorry :( , you ran out of tries. The word was " , word ,". Better luck next time!")    
     
    
    



            
def printHangman(turns):
  stages = [  
           """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     / \\
              -
           """,
           
           """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     / 
              -
           """,
           
           """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |      
              -
           """,
           
           """
              --------
              |      |
              |      O
              |     \\|
              |      |
              |     
              -
           """,
       
           """
              --------
              |      |
              |      O
              |      |
              |      |
              |     
              -
           """,
           
           """
              --------
              |      |
              |      O
              |    
              |      
              |     
              -
           """,
           
           """
              --------
              |      |
              |      
              |    
              |      
              |     
              -
           """
    ]
  print(stages[turns])


def main():
    word = randword()
    guess(word)
    while input("Continue playing? (Y/N) ").upper() == "Y":
        word = randword()
        guess(word)


if __name__ == "__main__":
    main()              