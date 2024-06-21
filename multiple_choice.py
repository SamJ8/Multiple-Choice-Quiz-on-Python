import time
import random
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)


print(Fore.BLUE + """



███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗     ███████╗     ██████╗██╗  ██╗ ██████╗ ██╗ ██████╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║     ██╔════╝    ██╔════╝██║  ██║██╔═══██╗██║██╔════╝██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║     █████╗      ██║     ███████║██║   ██║██║██║     █████╗      ██║   ██║██║   ██║██║  ███╔╝ 
██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║     ██╔══╝      ██║     ██╔══██║██║   ██║██║██║     ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗███████╗    ╚██████╗██║  ██║╚██████╔╝██║╚██████╗███████╗    ╚██████╔╝╚██████╔╝██║███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
                                                                                                                                                                                                                                                                                                                    
""")

questions = ["How Much Percentage Of Earth’s Surface Is Covered By Water? ",
             "What is the largest ocean on Earth? ",
             "In which year did World War II end? ",
             "In the film “The Matrix,” what is the name of the computer programmer who becomes Neo? ",
             "The chemical symbol for the element gold? "] ## all my questions to be generated.

options = [["A. 51%","B. 61%","C. 91%","D. 71%"],
        ["A. Indian Ocean","B. Atlantic Ocean","C. Pacific Ocean","D. Arctic Ocean"],
        ["A. 1944","B. 1945","C. 1943","D. 1946"],
        ["A. Neo Anderson","B. Thomas Neo","C. Mr.Smith","D. Thomas Anderson"],
        ["A. Au","B. Ag","C. Fe","D. Hg"]] ## all of my options that will appear to the user to choose from


answers = ("D", "C", "B", "D", "A") ## these will be all my answers to correlate with the options to the questions
replay = "Y" ## replay variable so that the user can replay if they want too
score = 0 ## our score variable is set to 0
question_num = 0 ## question number variable set to 0 so it goes onto the next question

print(Fore.LIGHTMAGENTA_EX + "You'll be answering a total of 20 questions! Each correct answer will give you 5 points! For every wrong answer lose 2 points!")

while replay == "Y":
    print(input("\nPress enter when you're ready!"))
    score = 0
    for seconds in range(5, 0, -1): ## i used a timer so it counts down until the 
        print(seconds)
        time.sleep(1)

    while question_num < len(answers): 
        print("--------------------------")
        print(questions[question_num])
        for option in options[question_num]:
            print(option)

        while True:
            guess = input("Enter (A, B, C, or D): ").upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C or D")
        
       
        if guess == answers[question_num]:
            score += 5
            print("Correct!")
        else:
            print("Incorrect, minus 2 points!")
            score -=2
        question_num += 1



    print(f"\n\nYour final score: {score}/100")

    replay = input("Would you like to play again? Y/N?: ").upper()
    question_num = 0

print("Thanks for playing!")

