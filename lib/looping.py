#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1  
        if i == 0:
            print("Happy New Year!")

happy_new_year()
           
def square_integers(int_list):
    integers = int_list
    new_integers = list()

    for integer in integers:
        new_integer = integer * integer 
        new_integers.append(new_integer)
    
    return new_integers

result = square_integers([1, 2, 3, 4, 5]) 
print(result)     

def fizzbuzz():
    num = 1

    while num <= 100:
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

        num += 1

fizzbuzz()
        
