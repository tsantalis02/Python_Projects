import random

def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    while valid_choice(player) == False:
        player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    choices = ['r','s','p']
    opponent = random.choice(choices)
    winner = 0 
    score01 = 0
    score02 = 0
    win = False
    while win == False:
     if player == opponent:
        print(f"Its a Tie! Choice is {opponent}")
     else:   
      if check_win(player, opponent):
        print(f"Yay! you won! Choice is {opponent}")
        winner = 1
      if check_win(player, opponent) != True:
        print(f"You lost! Choice is {opponent}")
        winner = 2
      score01,score02 = scorekeeper(score01,score02,winner)
      if score01 == 3 or score02 == 3:
          win = True
     if win == False:     
      player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
      while valid_choice(player) == False:
          player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ") 
      opponent = random.choice(choices)    
    return score01,score02  
     
def valid_choice(p_choice):
    if p_choice == 'r' or p_choice == 's' or p_choice == 'p' :
        return True
    else:
        return False
    
def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

def scorekeeper(score_01,score_02,winner):
    if winner == 0:
        return score_01,score_02
    if winner == 1:
        score_01 += 1
    if winner == 2:
        score_02 += 1
    return score_01,score_02


score_01,score_02 = rock_paper_scissors()
print()
if score_01 > score_02:
    print("You won :)")
else:
    print("You lost :(")
print("------------------")    
print("Final score:",score_01,"-",score_02)   

