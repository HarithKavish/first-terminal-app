def login():
    print("Attempt ",attempt,"\n")
    un=input("Username : ")
    pw=input("Password : ")
    if un=="Harith" and pw=="Harith":
        print("------------------------------------------------------")
        print("Logged In ...")
        print("Welcome Back",un)
        prh()
    else:
        print("\nUsername or Password is wrong !!!")
        print("---------------------------")
        login()
def cont():
    cont=int(input("Do You Want To Continue ?\n___________________________\n1)Yes\n2)No\nYour Choice : "))
    if cont==1:
        global count
        count+=1
        prh()
    else:
        print("___________________________")
        logout=int(input("Do You Want To Logout ?\n1)Yes\n2)No\nYour Choice : "))
        if logout==1:
            print("------------------------------------------------------")
            print("Logged Out ...")
            global attempt
            attempt+=1
            login()
        elif logout==2:
            print("___________________________")
            clos=int(input("Do You Want To Close ?\n1)Yes\n2)No\nYour Choice : "))
            if clos==1:
                print("======================================================")
                print("Maed Applications Closed...")
                print("======================================================")
            if clos==2:
                print("------------------------------------------------------")
                attempt+=1
                login()
def printname():
    print("1)Print Your Name :\n")
    i=input("Enter Your Name : ")
    print("Your Name       :",i)
    print("___________________________")
def calcu():
    print("2)Calculator :\n")
    calcu1=int(input("Enter the 1st number : "))
    calcu2=int(input("Enter the 2nd number : "))
    print("___________________________")
    print("Sum        : ",calcu1+calcu2)
    print("---------------------------")
    print("Difference : ",calcu1-calcu2)
    print("---------------------------")
    print("Product    : ",calcu1*calcu2)
    print("---------------------------")
    print("Quotient   : ",calcu1/calcu2)
    print("___________________________")
def prh():
    global count
    print("======================================================")
    print("              MAED APPLICATIONS            ","Sl.no:",count)
    ch=int(input('''
------------------------------------------------------
1)Print Your Name
2)Calculator\n___________________________
Enter Your Choice :'''))
    print("___________________________")
    if ch==1:
        printname()
    elif ch==2:
        calcu()
    else:
        print("Invalid Choice...")
        print("___________________________")
    cont()
count=1
attempt=1
login()
