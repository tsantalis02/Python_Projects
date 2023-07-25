import random 
from words import word_list

def randword():
    word = random.choice(word_list)
    return word

def guess(word):
    completeword = "_" * len(word)
    guessed = False
    guessedletters = []
    guessedwords = []
    guesses = 6
    print("Hangman! Let's start!")
    printHangman(guesses)
    print(completeword)
    print()
    while not guessed and guesses > 0:
        g = input("Guess a letter or a word: ")
        if len(g) == 1 and g.isalpha():
            if g in guessedletters:
                print("You already guessed the letter", g)
            elif g not in word:
                print(g, "is not in the word.")
                guesses -= 1
                guessedletters.append(g)
            else:
                print("Good job,", g, "is in the word!")
                guessedletters.append(g)
                word_as_list = list(completeword)
                ind = [i for i, letter in enumerate(word) if letter == g]
                for index in ind:
                    word_as_list[index] = guess
                completeword = "".join(word_as_list)
                if "_" not in completeword:
                    guessed = True
        elif len(g) == len(word) and g.isalpha():
            if g in guessedwords:
                print("You already guessed the word", g)
            elif g != word:
                print(g, "is not the word.")
                guesses -= 1
                guessedwords.append(g)
            else:
                guessed = True
                completeword = word            
        else:
          print("Not a valid guess.")
          print(printHangman(guesses))
          print(completeword)
          print()
          if guessed:
            print("Congrats, you guessed the word! You win!")
          else:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")



            
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
           #
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
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = randword()
        guess(word)


if __name__ == "__main__":
    main()              