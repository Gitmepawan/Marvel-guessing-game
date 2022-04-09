
from tkinter import image_names
from gameComponents import design, gameQuestions 
print(design.marvellogo)
print(design.welcome)
answer=input('Are you ready ? (y/n) :')
score=0
total_questions=4
 
def start_game(): # new game first
    guess = []
    play_n = 4
    correct_guess = 0
    for t in gameQuestions.answers[play_n-1]:
            print(t)
        guess = input("Enter (A or B or C or or D----------------): ")
        guess = guess.lower()



    if answer.lower()=='A':
        score += 1
        
        
        print('correct')
    else:
        print('Wrong Answer :(')
        
 
 
    
    if answer.lower()=='B':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
            
 
    
    if answer.lower()=='C':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
       
        
    if answer.lower()=='C':
        score += 1
        print('correct')
    
    else:
        print('Wrong Answer :(')
 
  
  
  
  def calc_score(): # new game first
      mark=(score/total_questions)*100

print(design.quit, flush=False)
mark=(score/total_questions)*100
print('Marks obtained:',mark)
