# Numericals to Words
print("Number to Number Name Programme")
print("----------------------------------------------------------------")
command='retry'
def numtoname(num):
    if num==1:
        name="One "
    if num==2:
        name="Two "
    if num==3:
        name="Three "
    if num==4:
        name="Four "
    if num==5:
        name="Five "
    if num==6:
        name="Six "
    if num==7:
        name="Seven "
    if num==8:
        name="Eight "
    if num==9:
        name="Nine "
    if num==0 or num=="0":
        name=""
    if num==10:
        name="Ten "
    if num==11:
        name="Eleven "
    if num==12:
        name="Twelve "
    if num==13:
        name="Thirteen "
    if num==14:
        name=="Fourteen "
    if num==15:
        name="Fifteen "
    if num==16:
        name="Sixteen "
    if num==17:
        name="Seventeen "
    if num==18:
        name="Eighteen "
    if num==19:
        name="Nineteen "
    if num==20 or num=="2":
        name="Twenty "
    if num=="3":
        name="Thirtry "
    if num=="4":
        name="Forty "
    if num=="5":
        name="Fifty "
    if num=="6":
        name="Sixty "
    if num=="7":
        name="Seventy "
    if num=="8":
        name="Eighty "
    if num=="9":
        name="Ninety "
    return name
while True:
    print("Type 'help' to get help,'number' to try the programe,'quit' to quit")
    command=input(">>> ")
    if command=='number':
        num=input("Enter a number:  ")
        if len(num)>=4:
            print(numtoname(int(num[-4])),"Thousand ",end="")
        if len(num)>=3:
            print(numtoname(int(num[-3])),end="")
            if int(num[-3])!=0:
                print("Hundred ",end="")
            if int(num[-2])!=0 or int(num[-1])!=0:
                print("and ",end="")
        if len(num)>=2:
            last2=int(num[-2]+num[-1])
            if 20>=last2>=10:
                print(numtoname(last2),end="")
            else:
                print(numtoname(num[-2]),end="")
        if len(num)>=1 and not 20>=last2>=10:
            print(numtoname(int(num[-1])))
    elif command=='help':
        print("Welcome to the Number Name Programme")
        print("Enter any number between 1 and 9,999 and get its number name")
        print("Type 'number' to try!")
    elif command=='quit':
        break
    else:
        print("Kindly enter a valid value!")
#Coded By
#Yours Truly
#TanX (Tanish Jain)
