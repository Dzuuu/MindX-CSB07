# def is_prime(a):
#     for i in range (2,a):
#         if a % i == 0:
#             return True
#     return False

# num = int(input("Input a number:"))
# if is_prime(num):
#     print(f'{num} is not a prime')
# else:
#     print(f'{num} is a prime')



def is_prime(a):
    for i in range (2,a):
        if a % i == 0:
            return True
    return False
num_input = int(input("Input number: "))
num_prime = 0
print(f'First {num_input} prime(s)')
k = 2
while num_prime < num_input:
    if is_prime(k) == False:
        print(k,end=" ")
        num_prime+=1
    k += 1



