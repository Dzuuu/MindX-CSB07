# Part1
# FirstName = input("First Name: ")
# LastName = input("Last Name: ")
# print(f'Your full name is {FirstName} {LastName}')

# inp = input("Your input: ")
# print(inp.upper())

# num1 = float(input("Input a number: "))
# print(num1**2)

# import turtle
# turtle.circle(100)



# Part 2
# print(3,4,5,6,7,8,9,10,11,12)

# num2 = int(input("Input a number: "))
# for x in range(0,num2+1):
#     print(x, end = " ")

# num3 = int(input("Input a number: "))
# for x in range(num3):
#     if x%2 != 0:
#         print(x)

# import turtle
# t = turtle.Turtle()
# edges = int(input("Input number of edges: "))
# length = int(input("Length of sides:  "))
# for x in range(edges):
#     turtle.forward(length)
#     turtle.right(360/edges)

# Part 3
# num4 = float(input("Input a number: "))
# if num4 > 13:
#     print("This number is larger than 13")
# else:
#     print("This number is not larger than 13")

# num5 = float(input("Input a number: "))
# if num5%2 == 0:
#     print("This number is even")
# else:
#     print("This number is not even")

# month = int(input("Input a month: "))
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print("This month has 31 days")
# else:
#     print("This month does not have 31 days")

# Part 4
print("== Registration ==")
Username = input("Input an email: ")
x = Username.split("@.")
Password = input("Input a password: ")
RePassword = input("Repeat password above: ")
if Password == RePassword:
    print("Registered successfully.")
elif Password != RePassword:
    print("Passwords do not match")
