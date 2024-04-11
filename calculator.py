print("Easy Calc")
math_type = input("Would you like to do 1) Addition, 2) Subtraction, 3) Multiplication, 4) Division? Please enter 1, 2, 3, or 4")

num1 = input("Please enter your first number")
num2 = input("Please enter your second number")
num1 = float(num1)
num2 = float(num2)

# print(num1, " ... ", num2)
# print(type(num1), type(num2))


def addition_math():
    answer = num1 + num2
    print(answer)

def do_math():
    if(math_type == "1"):
        addition_math()
    elif(math_type == "2"):
        #do subtraction
        pass
    else:
        print("More to figure out here.")

do_math()

math_type = input("Would you like to do more math? Please Enter Yes or No")

No = print("Have a great day!")
Yes = math_type = input("Would you like to do 1) Addition, 2) Subtraction, 3) Multiplication, 4) Division? Please enter 1, 2, 3, or 4")

num1 = input("Please enter your first number")
num2 = input("Please enter your second number")
num1 = float(num1)
num2 = float(num2)

# print(num1, " ... ", num2)
# print(type(num1), type(num2))


def addition_math():
    answer = num1 + num2
    print(answer)

def do_math():
    if(math_type == "1"):
        addition_math()
    elif(math_type == "2"):
        #do subtraction
        pass
    else:
        print("More to figure out here.")

do_math()