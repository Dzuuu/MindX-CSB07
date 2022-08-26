# scores = [5, 6, 6.5, 10]
# print(scores[2])
# print(len(scores))
# scores.append('abc')
# print(scores)

# i = 1
# for item in range(len(scores)):
#     print(f'item:{scores[i]}')
#     i+=1

str = input("Input something: ")
listDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
a = 0
for item in str:
    if item not in listDigit:
        a += 1
if a == 0:
    print("It is a digit")
else:
    print("It is not a digit")
