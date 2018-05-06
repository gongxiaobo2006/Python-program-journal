import turtle 

test = turtle.Turtle()
# 抬起画笔，向前运动一段距离放下  
def Skip(step):  
    test.penup()  
    test.forward(step)  
    test.pendown()  

test.penup()
test.goto(-300,0)
test.pendown()

test.speed(5)
#L
test.right(90)
test.forward(200)
test.left(90)
test.forward(100)

#间隔
Skip(70)

#O
test.forward(100)
test.left(90)
test.forward(200)
test.left(90)
test.forward(100)
test.left(90)
test.forward(200)
test.left(90)
test.forward(100)

#间隔
Skip(70)


#V
test.penup()
test.forward(100)
test.pendown()
test.left(111.9)                                       
test.forward(220)
test.backward(220)
test.right(111.9)
test.left(68.1)
test.forward(220)
test.backward(220)
test.right(68.1)
test.penup()
test.forward(100)
test.pendown()

#间隔
Skip(70)


#E
test.forward(100)
test.backward(100)
test.left(90)
test.forward(100)
test.right(90)
test.forward(100)
test.backward(100)
test.left(90)
test.forward(100)
test.right(90)
test.forward(100)


turtle.done()