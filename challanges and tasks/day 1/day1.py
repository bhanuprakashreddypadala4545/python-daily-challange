name=input("Enter your name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")
mobile=input("Enter your mobile number: ")
valid=1
if name[0]==" " or name[len(name)-1]==" " or name.count('')<1:
    valid=0
x=email.count('@')
y=email.count('.')
if x<1 or y<1 or name[0]=='@':
    valid=0
if len(mobile)!=10 or mobile[0]=='0' or mobile.isdigit()==False:
    valid=0
if age<18 or age>60:
    valid=0
if valid==1:
    print("user profile is valid")
else :
    print("user profile is invalid")
