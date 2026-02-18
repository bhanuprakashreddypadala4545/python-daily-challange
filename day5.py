n=int(input("enter number of integers:"))
requests=[]
for i in range(n):
    print("enter value:")
    requests=requests+[int(input())]
invalid_demand=[]
low_demand=[]
moderate_demand=[]
high_demand=[]
no_demand=0
valid=0
count=0
for i in range(n):
    if requests[i]<0:
        invalid_demand=invalid_demand+[requests[i]]
    elif requests[i]==0:
        no_demand+=1
        valid+=1
    elif 0<requests[i]<=20:
        low_demand=low_demand+[requests[i]]
        valid+=1
    elif 20<requests[i]<=50:
        moderate_demand=moderate_demand+[requests[i]]
        valid+=1
    else:
        high_demand=high_demand+[requests[i]]
        valid+=1
name="bhanuprakashreddypadala"
l=len(name)
pli=l%3
if pli==0:
    count=len(low_demand)
    low_demand=[]
elif pli==1:
    count=len(high_demand)
    high_demand=[]
else:
    count=len(low_demand)+len(high_demand)
    low_demand=[]
    high_demand=[]
print("length of name: ",l)
print("personalization",pli)
print("total valid requests: ",valid)
print("removed requests due to PLI",count)
print("low demand",low_demand)
print("moderate demand",moderate_demand)
print("high demand",high_demand)
