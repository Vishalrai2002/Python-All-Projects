from time import* 
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_Roundoff=round(time_delay,2)
    speed=len(userinput)/time_Roundoff
    return round(speed)


if __name__ == '__main__':
    while True:
        check=input("Ready to begin: yes or no :")
        if check=='yes':
            test=["Hello how are you guys","now i am learning python","i am also preparing for my placements"]

            test1=r.choice(test)

            print("     ******  Typing Speed  ******")
            print(test1)
            print()
            print()

            time_1=time()
            testinput=input("Enter : ")
            time_2=time()

            print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")

            print('Error : ',mistake(test1,testinput))
        elif check=="no":
            print("Thanks you for using it!")
            break
        else:
            print("wrong input")
            break
