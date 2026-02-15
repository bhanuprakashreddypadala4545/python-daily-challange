m=int(input("enter the no.of activity scores :"))
n=[0]*m
for i in range(m):
    n[i]=int(input("enter activity score :"))
registration_number="24110011666"
d=int(registration_number[-1])
print("your  last digit of your registration number is :",d)
low_risk=[]
med_risk=[]
high_risk=[]
critical_risk=[]
ignored=0
valid=0
for i in n  :
    if i<0:
        ignored=ignored+1
        continue
    valid=valid+1
    if i<=30:
        low_risk=low_risk+[i]
    elif i<=60:
        med_risk=med_risk+[i]
    elif i<=100:
        high_risk=high_risk+[i]
    else :
        critical_risk=critical_risk+[i]
print("before categorized the lists are")
print("low_risk :",low_risk)
print("med_risk :",med_risk)
print("high_risk :",high_risk)
print("critical_risk :",critical_risk)
if(d%2==0):
    removed=len(low_risk)
    low_risk=[]
else:
    removed=len(critical_risk)
    critical_risk=[]
print("after personlized filtering")
print("low_risk :",low_risk)
print("med_risk :",med_risk)
print("high_risk :",high_risk)
print("critical_risk",critical_risk)
print("total valid entries:",valid)
print("total ignored entries:",ignored)
print("removed due to personlization :",removed)

