lis=[]
class Complex:
    no_of_instances=0
    __real=0
    __img=0
    def __init__(self,real,img):
        self.real=real
        self.img=img
        Complex.no_of_instances+=1
    def add(self,other):
        real=self.real+other.real
        img=(self.img+other.img)
        print("the addition of 2 numbers",real,"+",img,"i")
    def mul(self,other):
        r1=(self.real*other.real)-(self.img*other.img)
        i1=(self.real*other.img)+(self.img*other.real)
        print("the multiplication of 2 numbers",r1,"+",i1,"i")
    def ob(self):
        print("the instances of the class are",self.no_of_instances)
    def __repr__(self): 
        return ' (%s,%si)' % (self.real, self.img)     
               
        
        
        
        
n1=Complex(3,5)
n2=Complex(5,7)
n3=Complex(4,6)
lis.append(n1)
lis.append(n2)
lis.append(n3)
n1.add(n2)
n1.mul(n2)
n1.ob()

print(sorted(lis,key=lambda x:x.real ,reverse=True))
