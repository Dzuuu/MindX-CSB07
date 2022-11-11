# Ex1
# a1 = int(input("Input first number: "))
# a2 = int(input("Input second number: "))
# c = a1 + a2
# print(f"{a1}+{a2} = c")

# Ex2
# import math
# a = float(input("Input a: "))
# b = float(input("Input b: "))
# c = float(input("Input c: "))
# delta = (b**2)-(4*a*c)
# sol1 = (-b-math.sqrt(delta))/(2*a)
# sol2 = (-b+math.sqrt(delta))/(2*a)
# if delta < 0:
#     print("No solution")
# elif delta == 0:
#     print(f"Same solution: {sol1} ")
# elif delta > 0:
#     print(f"The solutions are {sol1} and {sol2}")

# Ex3
# text2 = input("Input a text: ")
# def is_palindrome(n):
#     temp = []
#     t = ""
#     for i in n:
#         temp.append(i)
#     for i in range(1, len(temp)+1):
#         t += temp[-i]
#     if t == n:
#         print("This is a palindrome")
#     else:
#         print("This is not a palindrome")
# is_palindrome(text2)

# Ex7
# mylist = [5,1,8,92,-1,30]
# for i in range(len(mylist)):
#     for j in range(i+1,len(mylist)):
#         if mylist[i] > mylist[j]:
#             temp = mylist[i]
#             mylist[i]=mylist[j]
#             mylist[j]=temp
# print(mylist)

# Ex5
# Smartphones = {
#     "Iphone12": 28000000,
#     "Samsung N10": 16000000,
#     "Oppo 93": 7500000,
#     "Vsmart": 7400000,
#     "Vivo": 4200000
# }
# text1 = input("Input a name of a phone: ")
# print(Smartphones[text1])
# max = int(input("Input your budget: "))
# for item in Smartphones.values():
#         if max < item:
#             break
# for item in Smartphones.values():
#     if max > item:
#         print("item")

# Ex6
# number1 = int(input("Enter number: "))
# a = 0
# while(number1 > 0):
#     a=a+1
#     number1=number1//10
# print(f"This number has {a} digit(s)")

# Ex8
# numfibo = int(input("Print a number: "))
# n1 = 1
# n2 = 1
# demso = 0
# if numfibo <= 0:
#    print("Enter a positive number")
# elif numfibo == 1:
#    print(f"First {numfibo} numbers: ")
#    print(n1)
# else:
#    print(f"First {numfibo} numbers: ")
#    while demso < numfibo:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        demso += 1

