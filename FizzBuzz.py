#example of python projects
#questions from https://github.com/greyli/PythonExercises
#FizzBuzz.py

a=range(0,100)

for i in range(100):

    x = a[i]/3
    y = a[i]/5

    xint = int(x)
    xdec = x - xint

    yint = int(y)
    ydec = y - yint

    if xdec == 0 and ydec == 0: 
        print("FizzBuzz")       
    elif xdec == 0 and ydec != 0:
        print("Fizz")
    elif xdec != 0 and ydec == 0:
        print("Buzz")       
    else:
        print(a[i])
