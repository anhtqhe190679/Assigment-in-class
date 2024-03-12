
def Input_list():
    n = int(input('Enter the number of employees: '))
    lst=[]
    for i in range (n):
        e = employee()
        e.inputEmployee()
        lst.append(e)
    return lst
    
class employee:
    def inputEmployee(self):
        self.name = input('Name: ')
        self.salary = input('Salary: ')
        self.age = int(input('Age: '))
    def printEmployee(self):
        print('Employee')
        print(self.name)
        print(self.salary)
        print(self.age)

employeelist = Input_list()
def f1():
    print('f1----------------------------------------------------')
    for x in employeelist:
        x.printEmployee()
    print('f2----------------------------------------------------')
    employeelist.sort(key = lambda x : x.age, reverse = True)
    for x in employeelist:
        x.printEmployee()

def f3():
    print('f3-----------------------------------------------------')
    lst = []
    for i in employeelist:
        if (i.age > 18):
            lst.append(i)
    lst.sort(key = lambda i : i.salary, reverse = True)
    for i in lst:
        i.printEmployee()
        
f1()
f3()
        

    