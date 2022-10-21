# Ex3
fibonacci = [1,1]
num = int(input("Input a positive number: "))
print('First 1 Fibonacci number(s): ')
if num<=2:
    for i in range(num):
        print(fibonacci[i])
else:
    for i in range(2,num):
        fibonacci.append(fibonacci[i-1]+fibonacci[i+2])
