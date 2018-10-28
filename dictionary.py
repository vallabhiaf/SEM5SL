print("enter no. of students")
avg=0
n= int(input())
dic ={}
print("enter student_name,marks of three subjects")
for i in range(n):
    print("enter details of student ")
    usn =input()
    name =input()
    m1 =int(input())
    m2 =int(input())
    m3 =int(input())
    dic.setdefault(usn,[]).append(name)
    dic.setdefault(usn,[]).append(m1)
    dic.setdefault(usn,[]).append(m2)
    dic.setdefault(usn,[]).append(m3)
print("average marks of students:")
for x in dic:
     print(dic[x][0])
     avg=(dic[x][1]+dic[x][2]+dic[x][3])/3
     if(avg>50):
      print(avg)
print("details of student whose name start with character 'a'")
for x in dic:
    if dic[x][0][0] =='a' or dic[x][0][0] =='A':
        print(x)
        print(dic[x][0])
        print(dic[x][1])
        print(dic[x][2])
        print(dic[x][3])   
