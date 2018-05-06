#example of python projects
#questions from https://github.com/greyli/PythonExercises
#Guess number.py



import random
a = random.randint(0,100)
running = True
while running:
    val = input('please type in the number(e.g.:50),\
and the system will infer you the number is big or small:')
    x = int(val)
    if x == a:
        print("your answer is correct")
        running = False
    elif x > a:
        print("input is bigger than answer")
           
    elif x < a:
        print("input is smaller than answer")
       
    else:
        print("typo")
        
