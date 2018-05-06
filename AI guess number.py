#example of python projects
#questions from https://github.com/greyli/PythonExercises
#AI to guess number.py


val = input("please type in number(<100) that you want me to guess(e.g:90):")
val = int(val)
running = True
i = 1
x = 50
y = 49
while running:
    print('running times={0}'.format(i))
    if x == val:
        print('answer is: {0}'.format(x))
        running = False
    elif y == val:
        print('answer is: {0}'.format(y))
        running = False
    else:
        i=i+1
        x=x+1
        y=x-1
        
