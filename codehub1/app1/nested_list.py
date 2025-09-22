# lst1 = [[1,2,3],[4,5,6],[7,8,9]]
# lst2 = [[4,5,6],[1,2,3],[1,2,3]]

lst1=[]
size = int(input("enter the size:"))

for i in   range(size):
    d = []
    for j in range(size):
        x = int(input("enter value"))
        d.append(x)
    lst1.append(d)
lst2=[]
size = int(input("enter the size:"))

for i in range(size):
    d = []
    for j in range(size):
        x = int(input("enter value"))
        d.append(x)
    lst2.append(d)
print(lst1)
print(lst2)
lst3=[]
for i in range(3):
    dummy = []
    for j in  range(3):
        sum = lst1[i][j] + lst2[i][j]
        dummy.append(sum)
    lst3.append(dummy)
print(lst3)