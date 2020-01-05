#!/usr/bin/python3

name=input('What is your name? ')
age=input('What is your age? ')
dog=int(age) * 8
age2050=int(age)-2019+2050
ageNow=2019-int(age)

print('')
print('Hello,', name.capitalize())
print('You are', age , 'years old')
print("If you were a dog, you would be", dog)
print('You were born in', ageNow)
print("In 2050, you will be", age2050)
print('')
