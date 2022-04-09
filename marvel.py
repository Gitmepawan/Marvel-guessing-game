import os
from gameComponents import design, gameQuestions 


def start_game(): # new game first
    guesses = []
    question_num = -1
    correct_guess = 0
   
    
    for key in gameQuestions.questions:
    
        print(design.marvellogo)
        print(design.welcome)
        print(key)
        for t in gameQuestions.options[question_num+1]:
            print(t)
        guess = input("please Enter A or B or C or D:::::")
        guess = guess.upper()
        guesses.append(guess)
        correct_guess = game_answer(gameQuestions.questions.get(key), guess)
        question_num = 1

    display_score(correct_guess, guesses)

    
    
# answer correct or not
def game_answer(answer, guess):

    if answer == guess:
        
       
        if answer == "A":
            filename = "Documents/img_ir.jpg"
            image = image.open("image2")
            image.open()
      
            return 1
        elif answer == "B":
            image = image.open("image3")
            image.open()
            return 1
        elif answer == "D":
            image = image.open("image4")
            image.open()
            return 1
        else :
            image = image.open("image5")
            image.open()
            return 1   
    else: 
        
                        return 0
     
# this function will show the scores
def display_score(correct_answers, guesses):
   
    print(design.marvellogo)
    print(design.welcome)
    print(design.quit)
    print("                          correct answers ", end="")       
    for t in gameQuestions.questions:
        print(gameQuestions.questions.get(t), end=" ")
    print()

    print("                           Your guesses ",  end="")
    for t in guesses:
        print(t, end=" ")
    print()
   

# function to ask to play again?
def new_game():
    response = input("Press (Y) to play again, Any key to quit\n")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False
start_game()

while new_game(): # new game function
   start_game()
print(design.marvellogo)
print(design.welcome)
print(design.quit)
