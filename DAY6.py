n=int(input("Enter number of transactions: "))
trans_list=[0]*n
for i in range(n):
    trans_list[i]=int(input("Enter transaction amount: "))
trans_types={
"invalid":[k for k in trans_list if k<=0],
"normal":[k for k in trans_list if k>0 and k<=500],
"large":[k for k in trans_list if k>500 and k<=2000],
"high_risk":[k for k in trans_list if k>2000],
}
valid_trans=[k for k in trans_list if k>0]
count_valid=len(valid_trans)
total=0
for k in valid_trans:
    total+=k
if len(trans_list)>10:
    print("Frequent Transactions")
if total>100000:
    print("Large Spending")
if len(trans_types["high_risk"])>=5:
    print("Suspicious Pattern")
risk="Low Risk"
if count_valid>4 and total>50000:
    risk="High Risk"
elif count_valid>3 or total>25000 or len(trans_types["high_risk"])>=5:
    risk="Moderate Risk"

print("Invalid:",trans_types["invalid"])
print("Normal:",trans_types["normal"])
print("Large:",trans_types["large"])
print("High Risk:",trans_types["high_risk"])
print("Total transaction value:",total)
print("Number of transactions:",len(trans_list))
print("Risk Classification:",risk)
summary=(len(trans_list),count_valid,total,risk)
print("Summary:",summary)