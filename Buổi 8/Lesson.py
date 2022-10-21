# import modul
# import modul1
# canh1,canh2,canh3 = modul.get_input()
# print(f'sum: {modul1.chu_vi(canh1,canh2,canh3)}')
# print(f'max: {modul1.max(canh1,canh2,canh3)}')


# car = {
#     "brand": "Toyota",
#     "year": 2010,
#     "price": 400.45,
#     "colors": ["grey", "red", "blue"]
# }
# print(type(car))
# print(car["price"])
# print(car.items())
# print(car.keys())
# print(car.values())
# for key in car.keys():
#     print(car[key])
# for key,valu in car.items():
#     print(f"{key}:{valu}")


from ipaddress import summarize_address_range


laptops = {
    "HP": "20",
    "DELL": "50",
    "MACBOOK": "12",
    "ASUS": "30"
}
print(laptops["HP"])
key = input("Input a laptop name: ")
print(laptops[key])

sum = 0
for key in laptops.key():
    sum += laptops[key]
print(sum)



