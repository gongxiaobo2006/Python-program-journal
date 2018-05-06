# self-learning for python book(from start to end)


'''
# test add function
name = str(input('Enter a your name: '))
state = " 'A person who never made a mistake never tried anything new.' "
statement = name +" "+"said" +" "+ state
print(statement)
'''

'''
# test append,delete and insert
motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

motorcycles.append('ducati')
print (motorcycles)

del motorcycles[1]
print (motorcycles)

motorcycles.insert(1,'lifan')
print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

print("\nA")

pizza = ['chorizo', 'pepperoni','cheese']

for lovepizza in pizza:
    statement = 'I like' + " " + lovepizza + ' pizza'
    print (statement)
    
for number in range(1,5):
    print(number)
'''

'''
# the step size is depend on the last number of the range
# 2 refers to stepsize equal to 2which can be used to indicate the even number
even_number = list(range(2,11,1))
print(even_number)
'''


#test for the number calculation
'''
digits = [1,2,3,4,5,6,10,100]
print(min(digits),max(digits))
'''

#example 4-3 to 4-9
'''for num in range (1,21):
    print(num)

list1 =[0]
for num1 in range (1,100):
    list1.append(num1)

print(list1)
'''
'''
4for num2 in range (1,20,2):
    print(num2)
'''

#test for dictionaries and lists
#idea here is my favortite foods and my friends' favorite foods have something
#in common, in the case, there is no need to crete two lists
#then only one list and append some other items
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)
print("\nMy friends' favorite foods are:")
print(friend_foods)
'''

#test for if statement
# upper statement refers to upper all characters
# title statment refers to upper only first character
'''
ars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
if car == 'audi':
    print("wa")
else:
    print("cai")
'''

# integer cmp
'''
answer = int(input("please enter a integer:"))
if answer != 42:
    print("That is not the correct answer. Please try again!")
'''

# example 5-1, condition test
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car = 'audi'?I predict False.")
print(car == 'audi')
'''

#example 5-3 alien color
'''
alien_color = 'red'
if alien_color == 'green':
    print("player gain 5 points")
elif alien_color != 'green':
    print("player gain 10 points")
'''

#5.4.1 example special items
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
'''

#5.4.2 example for determining the list
'''
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza？")
'''
#6.4.1 dictionary nest
'''
alien_0 ={'color':'green','points':5}
alien_1 ={'color':'yellow','points':10}
alien_2 ={'color':'red','points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''
'''
aliens=[]
alien_color=['red','yellow','green']

for alien_number in range(30):
    for color in alien_color:
        new_alien ={'color': alien_color[1], 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
'''
#6.4.2 list in dictionary
'''
#the name and languages here refers to the first part of dictionary and second part
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
'''

#6.4.3 store dictionary into dictionary
'''
users = {
    'Allie':{
        'first_name':'wei',
        'last_name':'tang',
        'location':'hong kong',
            },
    'Oliver':{
        'first_name':'peihan',
        'last_name':'li',
        'location':'shen zhen',
            },
        }
for username,user_info in users.items(): #items ,'s' important
    print("\nUsername: "+username)
    full_name = user_info['first_name']+" "+user_info['last_name']
    #importance: every list should be put toghther with user_info
    location = user_info['location']

    print("\tFull name: "+ full_name.title())
    print("\tlocation: "+ location.title())
'''
#7.1.3 mod operator
#calculate the division of two numbers and return the remainder
'''
x = 5 % 3 # the remainder should be the output which is 2 in this case
print(x)
'''

#7.2.1 while loop introduction
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''

#7.2.2 use choose the quit while loop
'''
prompt = "\nTelll me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)

    if message !='quit':
        print(message)
'''
#7.2.4 use break to exit while loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


#7.2.5 use continue in while loop
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #importance here, you should always make sure there is a way to avoid loop forever
    print(current_number)
'''
#7.3.2 delete all specific element
'''
pets = ['dog','dog','dog','cat','cat','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    print(pets)
#idea here is the remove instruction can only delete one element one time
#so we need to put it into the while loop to delete all the elements
'''

#8 functions












