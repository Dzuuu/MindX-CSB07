# Ex1
# print("List of names: ")
# with open(r"Buoi10\names.txt","r") as fi:
#     for i in fi.readlines():
#         print("-", end =" ")
#         print(i,end = "")


# list = ["a",1,True]
# for item in list:
#     print(item)

dict = {
    "key1": {
        "ten":"abc",
        "tuoi": 12,
        "diachi": "a1"
    },
    "key2": {
        "ten":"abc",
        "tuoi": 14,
        "diachi": "a2"
    },
    "key3": {
        "ten":"abc",
        "tuoi": 11,
        "diachi": "a3"
    }
}

max = 0
for item in dict.values():
    if max < item['tuoi']:
        max = item['tuoi']
for item in dict.values():
    if max == item['tuoi']:
        print(item['ten'])
        print(item['diachi'])