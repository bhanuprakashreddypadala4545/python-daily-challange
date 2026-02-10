
n=int(input("enter no.of students:"))
m=[0]*n
for i in range(n):
    m[i]=int(input("enter marks:"))
    name="bhanu"
    if len(name)<=5:
        m[i]-=1
    else:
        m[i]+=1
totalvalidstudents=0
totalfailstudents=0
for i in range(n):
    if m[i]<0 or m[i]>100 :
        print(m[i],"->invalid")
    else :
         totalvalidstudents+=1
         if m[i]>=90:
           print(m[i],"->excellent")
         elif m[i]>=75:
           print(m[i],"->verygood")
         elif m[i]>=60:
             print(m[i],"->good")
         elif m[i]>=40:
             print(m[i],"->average")
         else:
             totalfailstudents+=1
             print(m[i],"->fail")



print("total valid students are :",totalvalidstudents)

print("total fail students are:",totalfailstudents)
