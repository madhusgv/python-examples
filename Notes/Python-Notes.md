Links:
--------
1. askpython.com
2. docs.python.org
    - For Datastructure/Lists, 
3. https://www.geeksforgeeks.org
    - For Multiple examples for datastructures

01. Basics
===========
    - print function
        1. user '' or "" to print strings
        2. Use + to concadinate 
        3. ex: print("Hello World")
    - input function
        - used to read the input from console
        - ex: input("What is your name? ")
    - Use Thonny tool to debug python (https://thonny.org/)
    - len() function
        - Used to calculate lenght of the string
    - Python variables
        - variables are used to name a value
        - name the variable with meaning
02. Data Types
===============
    - Primitive Data types
        1. string
            - Subscripting string
                "Hello"[0] - Resurtns H
        2. integers
            ex: 123
                123_122_334 for large numbers(, ,. of ,)
        3. float
            ex: 123.43
    - Type Error
        1. type() - returns the type of the variable
    - Mathemetical operations
        - PEMDASLR
            1. () - Paranthesis
            2. ** : Exponential
            3. * :  Multiplication
            4. / : Division
            5. + : Addition
            6. - : Subtraction
            7. LR -Left to Right
    - Built-in functions
        > Using the Built-in functions convert one type to another type
        > Example functions
            - int(), float(), str(), etc.
        > Using the Built-in functions do the mathmetical operations
            - pow()
            - round()

    - BMI Calculator
        height = input("enter your height in m: ")
        heighti = float(height)
        weighti= float(weight)
        bmi = int(weighti / (heighti*heighti))
        print(bmi)
    - F Strings
        > Flow division - divide and return the result as int
            flowdivision_result = 8 // 3
        > Manipulatoin and assignment
            score = 0
            score+=1
            print(score)
        
        > fstrings is to mix multiple datatypes with strings
            score = 10
            height = 1.75
            isWinning = True
            print(f"your scrore is {score}, Your height is {height}, your winning status {isWinning}") --> fstring

3. Control Flow and Logical Operators
=========================================
    a. Conditional statements
        - Conditional Operators : ==, >, <, >=, <=, !=
        - if, else, elif
        example: if a == b:
                    print("In if condition")
                elif a > b:
                    print("In elif condition")
                else:
                    print("In else condition")

4. Ramonization and lists
===============================
    1. Ramdom Module
        - import random
        - random.randint(x,y) - returns random integer number between x and y
        - random.random() returns random float number 0.00000 to 0.999999
        if we want to generate random float number 0 to x , where x can be 5. then multiply the return
        random.ramdom()*5
    2. Lists
        - friuts = ["Apple", "Orange", "Cherry"]
        - positive index to acces the items from first
        - negative index to access to items from last
        - To add a item in list use append() method
            ex: fruits.append("Pineapple")
    3. IndexError and Nested Lists
        - If we access a list beyond limit then the index error will be returned
        - Nested lists are nothing but list inside a list.both lists have relationship.
            examples:
                veg = ['potato', 'brinjal']
                fruits = ['apple', 'grape']
                dirty_dozen = [veg, fruits]

5. Loops
==========
    1. executes statements multiple times
        - loop lists
          mylist = ['a','b','c']
        for myl in mylist:
            print(myl)
    2. Loop using range
        for number in range(1,10):
            print(number)

6. Functions
==============
    1. function
        def myfunction():
            print("I am in function")
    2. While loop
        - loop until the condition is met
    


    
