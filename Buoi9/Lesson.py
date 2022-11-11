# r - read files
# a - append
# w - viet luon vao file

f = open(r"Buoi9\text1.txt","r")
a = f.read()
b = []
for i in a.split(" "):
    b.append(int(i))
max = b[0]
for i in range(len(b)):
    if (b[i]>max):
        max = b[i]
print(max)