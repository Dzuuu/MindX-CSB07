# LIST AND TUPLE
# myList = [6,7,8]
# print(myList[0])
# myList2 = ["a","6","abc",6,True]
# print(type(myList2[4]))

# list = myList + myList2
# list.append("x")
# list.remove("6")
# list.remove(6)
# print(list)


# myList3 = [6,7,8,6,"orange"]
# myList3.remove(6)
# myList3.pop(2)
# print(myList3)

# for item in myList3:
#     print(item)

# for i in range(len(myList3)):
#     print(myList3[i])

# a = 0
# while a < 5:
#     print(myList3[a])
#     a +=1

# lisEx = list(("1",2))
# myList3.extend(lisEx)
# print(myList3)


# myTuple = (1,2,3,4)
# myTuple2 = tuple(("abcv","abcbcb"))
# myTuple = (15,)
# print(myTuple)

# a = 0
# while a < 4:
#     print(myTuple[a])
#     a += 1


sum = 0
list1 = [1, 2, 3, 4, 5]
for i in range(0, len(list1)):
    sum = sum + list1[i]
print(sum)

# number = [-5,-2,-4,-3,5,4,2,1]
# for i in range(len(number)):
#     for j in range(i+1,len(number)):
#         if number[i] > number[j]:
#             temp = number[i]
#             number[i]=number[j]
#             number[j]=temp
# print(number)