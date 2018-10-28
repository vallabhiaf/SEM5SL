list=[]
n=input("Enter string1:")
list.append(n)
n=input("Enter string2:")
list.append(n)
n=input("Enter string3:")
list.append(n)
print(list)
print("First five characters of str1:", list[0][0:5])
print("odd intervals:",list[1][::2])
print("Last 5 upper:", list[2][-5::1].upper())

print("Capitalize everything")
list1=[]
for i in list:
    list1.append(i.capitalize())
print(list1)
