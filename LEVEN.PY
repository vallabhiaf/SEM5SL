n = int(input("Enter the number of elements:"))
ele=[]
even=[]
odd=[]
for i in range (n):
    a = int(input("Enter the elements:"))
    ele.append(a)
    for i in (ele):
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
print("L E", max(even))
print("L O", max(odd))
