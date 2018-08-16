#1
a = []
x = int(input("enter the no of elements "))
for i in range(x):
    c=input("enter element")
    a.append(c)
print(a)


#2
b = ['google','apple','facebook','microsoft','tesla']
a.extend(b)
print(a)

#3
w = [2,3,4,1,2,3,4,3,3,5,3,3,3,4,5]
print(w.count(3))

#4
q = [3,2,6,7,9,5,34,56,78,98,76,102,67,152]
q.sort()
print(q)

#5
r =[1,2,3,4,5]
e=[6,7,8,9]
f=[]
r.extend(e)
f=r
r.sort()
print(r)

#6
#stack using list
lis = []
while(True):
    print("enter a number")
    option = int(input("enter the option"))
    if(option ==1):
        lis.append(input("enter the value in stack"))
    elif(option ==2):
        if len(lis)>0:
            lis.pop()
        else:
            print("stack is empty")
    elif(option ==3):
        print(lis)
    else:
        break
lis1 = []
while(True):
    print("enter a number")
    option = int(input("enter the option"))
    if(option ==1):
        lis1.append(input("enter the value in queue"))
    elif(option ==2):
        if len(li)>0:
            lis1.pop(0)
        else:
            print("queue is empty")
    elif(option ==3):
        print(lis1)
    else:
        break
#7
z=0
v=0
for i in lis:
    
    if(i%2==0):
        z=z+1
    if(i%2==1):
        v=v+1
print("number of even elements are "+z)
print("number of odd elements are "+v)

