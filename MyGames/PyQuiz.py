print("Welcome to AskPython Quiz")

answer=input("Are You Ready to Play the QUIZ ? (yes/no) :")
score=0
tot_q=3

if(answer.lower()=="yes"):
    answer=input("Question 1: Mention a Programming language which is easy to learn : ")
    if(answer.lower()=="python"):
        score+=1
        print("Correct Answer!")
    else:
        print("Wrong Answer :(")

    answer=input("Question 2: Do you Like PYTHON ? (yes/no) :")
    if(answer.lower()=="yes"):
        score+=1
        print("Correct Answer!")
    else:
        print("Wrong Answer :(")
    answer=input("Question 3:Python has Interpreter or Compiler ? :")
    if(answer.lower()=="interpreter"):
        score+=1
        print("Correct Answer!")
    else:
        print("Wrong Answer :(")
print("Thankyou for playingg the game...")
print("Your Score:",score)
mark=(score*100)/tot_q
print("Marks Obtained:",mark)
