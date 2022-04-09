
from tkinter import image_names
from gameComponents import design, gameQuestions 
print(design.marvellogo)
print(design.welcome)
answer=input('Are you ready ? (y/n) :')
score=0
total_questions=4
 
def start_game(): # new game first
    guess = []
    question_num = -1
    correct_guess = 0
    
   
if answer.lower()=='yes':
    answer=input('Question 1: "Who Breaks the Fourth Wall?"')
    if answer.lower()=='Deadpool':
        score += 1
        
        
        print('correct')
    else:
        print('Wrong Answer :(')
        
 
 
    answer=input('Question 2: "who can do Supersonic flights? " ')
    if answer.lower()=='B':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
            
 
    answer=input('Question 3: "which marvel character has stretchy pants?"')
    if answer.lower()=='C':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
       
        answer=input('Question 2: "WHich is character created by Stan Lee and Steve Ditko?"')
    if answer.lower()=='C':
        score += 1
        print('correct')
    
    else:
        print('Wrong Answer :(')
 
 
print('Thankyou for Playing this small guessing game, you attempted',score,"questions correctly!")


print(design.quit)
mark=(score/total_questions)*100
print('Marks obtained:',mark)
