a = input('Enter the movements of robot: ')
a = str(a).split(', ')
def f1():
    for i in a:
        print(i)
f1()
def f2():
    lst = [x.split() for x in a]
    x = int(lst[0][1]) - int(lst[1][1])
    y = int(lst[2][1]) - int(lst[3][1])
    b = (x**2 + y**2)**(1/2)
    print(round(b))
f2()
   
