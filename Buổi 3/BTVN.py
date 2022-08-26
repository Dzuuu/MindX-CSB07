# Ex1
# number = int(input("Input a random number: "))
# if number%2 == 0:
#     print(f"{number} is an even number")
# else: 
#     print(f"{number} is an odd number")

# Ex2
# number2 = float(input("Input number:"))
# if number2%1 == 0:
#     print(f'{number2} is an interger')
# else:
#     print(f'{number2} is not an interger')

# Ex3
# character = (input("Input character:"))
# if character.isdigit():
#     print(f'{character} is a digit')
# else:
#     print(f'{character} is not a digit')

# Ex4
# number4 = int(input("Input a random number: "))
# if number4%3 == 0 and number4%5 == 0:
#     print(f"{number4} is divisible by 3 and 5")
# elif number4%3 == 0:
#     print(f"{number4} is divisible by 3")
# elif number4%5 == 0:
#     print(f"{number4} is divisible by 5")
# else:
#     print(f"{number4} is not divisible by 5 and 3")

# Ex5
# print("Welcome to The Ultimate Sercurity System")
# username = input("Username: ")
# password = input("Password: ")
# if username == "admin" and password == 123456:
#     print("You are logged in.")
# else:
#     print("Wrong username or password.")

# Ex6
# a = float(input("Input length 1: "))
# b = float(input("Input length 2: "))
# c = float(input("Input length 3: "))
# if a + b > c and a + c > b and b + c > a:
#     print("The 3 line segments can form a triangle.")
# else:
#     print("The 3 line segments cannot form a triangle.")

# Ex7
a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))
if a*2 + b*2 == c*2 or a*2 + c*2 == b*2 or b*2 + c*2 == a*2:
    print("The 3 line segments can form a right angle triangle.")
elif a == b == c:
    print("The 3 line segments can form a equilateral triangle.")
    from turtle import*
    shape("turtle")
    forward(a)
    left(120)
    forward(b)
    left(120)
    forward(c)
    done()
elif a+b>c and a+c>b and b+c>a:
    print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")