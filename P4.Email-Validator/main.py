email=input("Enter your Email: ")
k=0
l=0 
m=0 
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if (email[-3]=='.') or (email[-4]=='.'):
                for i in email:
                    if i==i.isspace():
                        print('h1')
                        k=1
                    elif i==i.isalpha():
                        if i==i.upper():
                            print("h2")
                            l=1
                        elif i==i.isdigit():
                            continue
                        elif i=='.' or i=='@' or i=='_':
                            continue
                        else:
                            m=1
                if k==1 or l==1 or m==1:
                    print("Wrong Email 5")
                else:
                    print("Correct Email ")         
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")