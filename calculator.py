class calculator:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2
    def division(self):
        return self.num2/self.num2
print("Calculator")
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
object=calculator(num1,num2)
choice=1
while choice!=0:
    print('Enter 1 for addition: ')         
    print('Enter 2 for Subtraction: ')         
    print('Enter 3 for multiplication: ')         
    print('Enter 4 for division: ')    
    print("Enter 0 to exit ")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(object.add())  
    elif choice==2:
        print(object.subtract())
    elif choice==3:
        print(object.multi())
    elif choice==4:
        print(object.division())
    elif choice==0:
        print("Exiting Program")
    else:
        print('invalid Choice')
    
    
