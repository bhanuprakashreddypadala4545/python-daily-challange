studentid=input("Enter Studentid :")
emailid=input("Enter Emailid :")
password=input("Enter Password :")
referral=input("Enter Referral :")

if studentid[0:3]=="CSE" and studentid[3]=="-" and studentid[4:7].isdigit():
    if emailid.count("@")>=1 and emailid.count(".")>=1 and emailid[-4:]==".edu" and emailid[len(emailid)-1]!="@" and emailid[0]!="@":
        if len(password)>=8 and password[0].isupper() and (password.count ('0') or password.count ('1') or password.count ('2') or password.count ('3') or password.count ('4') or
                                                           password.count('5') or password.count('6') or password.count('7') or password.count('8') or password.count('9') ):
            if referral[0:3]=="REF" and referral[3:5].isdigit() and referral[5]=="@":
                print("APPROVED")
            else:
                print("REJECTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
