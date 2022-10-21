# numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
# numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
# numbers.update(numbers_2)
# numbers.update({"kk"})
# x = input("Input a Roman number: ")
# if x in numbers.keys():
#     print("Arabic number: ", numbers[x])
# else: 
#     print("Not found")





# Ex3
# number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
# 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
# if x in number_list:
#     print("Arabic number: ", number_list[x])
# else:
#     print("not found")    

# students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
# {'firstName': 'Mervin', 'lastName': 'Friedland'},
# {'firstName': 'Aron', 'lastName': 'Wilkins'}]
# print("List of students: ")
# print("+ ", students)

# Ex5
names = {
'students': [
   {'firstName': 'Nikki', 'lastName': 'Roysden'},
   {'firstName': 'Mervin', 'lastName': 'Friedland'},
   {'firstName': 'Aron', 'lastName': 'Wilkins'}
   ],
'teachers': [
   {'firstName': 'Amberly', 'lastName': 'Calico'},
   {'firstName': 'Regine', 'lastName': 'Agtarap'}
   ]
}

for x,y in names.items():
    print(f'List of {x}')
    for dic_name_person in y:
        print("-", end = " ")
        for name_person in dic_name_person.values():
            print(name_person,end =" ")
        print()
