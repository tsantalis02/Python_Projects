import random

def guess(lower,upper,guesses):
  x = random.randint(lower,upper)
  guessed = False
  count = 0
  while guesses != 0 and guessed == False:
      y = int(input("Guess (give an integer number): "))
      guesses -= 1
      count += 1
      if(y > x):
          print("Try Again! Your guess was too high.")
      elif(y < x):
          print("Try Again! Your guess was too low.") 
      else:
          print(f"Congratulations! You guessed the number in {count} guesses!")
          guessed = True
  if(guessed == False):
    print("Better Luck Next Time!")



#Test function
lower_bound = int(input("Give the lower bound of the range of numbers to guess: "))
upper_bound = int(input("Give the upper bound of the range of numbers to guess: "))
guess(lower_bound,upper_bound,5)        