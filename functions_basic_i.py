#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

    # Prediction: The console will print the number 5.


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

    # Prediction: The console will throw an error, because the function "number_of_days_in_a_week_silicon_or_triangle_sides()" has not yet been defined.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Prediction: The console will print 5. The function exits at the first return statement, so it will not move on to return 10.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# Prediction: The console will print 5. Again, the function exits at the "return" statement, so it will not move on to print 10.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

    # Prediction: Because the function "number_of_great_lakes" doesn't return a value, it won't work as the value of the variable x. The function "print(x)" may either throw an error or print "number_of_great_lakes()." I'm not entirely sure what will print, but I know that the console won't print 5.

    # Update: I was wrong about this one. When I ran the code,the console printed "5" and then "None". I'm guessing it prints "5" because the function "number_of_great_lakes" was called when defining the variable "x".

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

    # Prediction: Since the function "add(b,c)" doesn't include a return statement, it won't produce a value when add(1,2) and add(2,3) are called. Thus, the console will likely throw an error.

    # Update: When I ran the code, the console printed 3 and 5 before throwing an error. It seems that, even though add(1,2) + add(2,3) won't actually produce a value, calling those functions inside the print function will still print the sum of "b" and "c" each time.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

    # Prediction: The function turns "b" and "c" into a string. Since the arguments passed into the function are 2 and 5, the function will convert these numbers into strings and concatenate them. Thus, the console will print 25.  


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Prediction: The console will first print 100. Then it will print 10, since 100 is not less than 10. The console will not print 7, since the "else" statement ends the program after it is executed. 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# Prediction: The first time the function is called, the console will print "7", because 2 is less than 3. The second time the function is called, the console will print "14", because 5 is not less than 3, and the function executes the "else" condition. The third time the function is called, the console will print "21", because the first function call returns 7, and the second function call returns 14. The console will never print 3, since the function will always end after the "else" statement. 


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

    # Prediction: The console will print 8. The console will not print 10, because the function ends after the first return statement.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

""" Prediction: The console will print as follows:
    500 (because b is equal to 500)
    500 (even though the "foobar" function has been created, it has not been called, and so it doesn't affect the value of b)
    300 (the "foobar" function sets the variable "b" to 300)
    500 (even though the "foobar" function has been called, the variable "b" only changes inside the function. The "b" variable outside of the function remains unchanged)
"""


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

""" Prediction: The console will print as follows:
    500 (because "b" is equal to 500 at this point)
    500 (even though the print function occurs after the "foobar" function has been defined, the "foobar" function has not been called)
    300 ("b" has been set to 300 within the "foobar" function)
    500 (even though "b" was set to 300 in the "foobar" function and the function was set to return b, the "return" command does not affect the value of "b" outside of the function)
"""


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

""" Prediction: The console will print as follows:
    500 (because "b" has been set to 500)
    500 ("b" is still equal to 500, since the "foobar" function has not been called)
    300 ("foobar" returns a value of 300 for "b", and "b" has been reassigned the value that "foobar" sets)

    Update: when I ran the code, the console printed 500, 500, 300, 300. I'm guessing it printed the extra 300 since "foobar()" included a "print" command, which would have been executed when the variable "b" was set to equal "foobar()".
"""


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

""" Prediction: The console will print as follows:
    1 (the function "foo" has been called, and the first command in "foo" is to print 1)
    3 ("foo" runs the function "bar", which calls for printing 3)
    2 (this is the final command in the "foo" function)
"""


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

""" Prediction: The console will print as follows:
    10 (since "foo()" has become the value for "y", whatever it returns becomes what "y" is set to. "foo()" returns 10, and y = "foo()"; therefore, printing "y" will print 10)

    Update: The console actually printed 1, 3, 5, 10 on separate lines. When "foo()" was called as the value of "y", it ran "foo()". "foo()" first calls for printing 1 to the console. Then it calls the function "bar()" in order to set the value of "x". "bar()" first calls for printing 3. Then it returns 5, which becomes the value of "x". When "x" is printed, the console prints "5".
"""