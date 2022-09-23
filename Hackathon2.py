# Ex1
# list1 = ['blue', 'teal', 'green']
# print(f'Color list:')
# for item in list1[:-1]:
#   print(item, end=', ')
# print(list1[-1])
# newcolor = input("Input a new color: ")
# list1.append(newcolor)
# print(f'New list: ')
# for color in list1[:-1]:
#     print(color, end = ',')
# print(list1[-1])

# Ex2
# position = int(input("Input a position: "))
# print(f'Color at position {position}: {list1[position-1]}')
# delete = input("Item to delete: ")
# listDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
# a = 0
# for item in delete:
#     if item not in listDigit:
#         a += 1
# if a == 0:
#     list1.pop(int(delete)-1)
# else:
#     list1.remove(delete)
# for color in list1[:-1]:
#     print(color, end = ',')
# print(list1[-1])

# from turtle import *
# shape('turtle')
# pencolor('red')
# forward(20)
# pendown()
# forward(10)
# penup()
# pencolor('orange')
# forward(20)
# pendown()
# forward(10)
# penup()
# pencolor('yellow')
# forward(20)
# pendown()
# forward(10)
# penup()
# pencolor('green')
# forward(20)
# pendown()
# forward(10)
# penup()
# pencolor('blue')
# forward(20)
# pendown()
# forward(10)
# penup()
# pencolor('violet')
# forward(20)
# pendown()
# forward(10)
# penup()

# Ex3
# list2 = ['1','3','6','10','20']
# find = input("Input a random number: ")
# a = 0
# for item in list2:
#     if item == find:
#         a+=1
# if a == 0:
#     print("Number not found")
# else:
#     print("Number found") #E ko biết cách tìm position ;-;

# sum = 0
# listsum = [1,4,6,7,10]
# for i in range(0, len(listsum)):
#     sum = sum + listsum[i]
# print(f'The sum of all numbers in listsum is: {sum}')

# sumlist = 0
# while True:
#     list = int(input("Input a list of number: "))
#     if list == 0:
#         break
#     sumlist += list
# print(f'Sum of all the number in the list:', sumlist)

# Ex4
# list5 = [1,2,3,4,5]
# for item in list5:
#     if item % 2 == 0:
#         print("Even number: ", item)

# evenList = []
# while True:
#     list = int(input("Input a list of number: "))
#     if list == 0:
#         break
#     if list%2==0:
#         evenList.append(list)
# for item in evenList:
#     print(item, end = ',')

# Ex5
# districts = ['BD','BTL','CG','DD','HBT']
# citizens = [247100, 333300,266800,420900,318000]





# Ex7
# highScores = [78,56,67]
# print(f"Highscores: {highScores}")
# newScore = int(input("Input new score: "))
# highScores.append(newScore)
# print(f"New Highscores: {highScores}")

# Ex8
# highScores = [78,56,67]
# print(f"Highscores: {highScores}")
# newScore = int(input("Input new score: "))
# highScores.append(newScore)
# highScores.sort(reverse=True)
# print(f"New Highscores: {highScores}")

# highScores2 = [78,68,59,90,200]
# newScore2 = int(input("Input new score: "))
# highScores2.append(newScore2)
# highScores2.sort(reverse=True)
# highScores2 = highScores2[:5]
# print(highScores2)









