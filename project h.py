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
            print("------------------------------------------------------")
            clos=int(input("Do You Want To Close ?\n1)Yes\n2)No\nYour Choice : "))
            if clos==1:
                print("======================================================")
                print("Maed Applications Closed...")
                print("======================================================")
            if clos==2:
                print("------------------------------------------------------")
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

def cap():
    a1=[[" 1111 ","11  11","111111","11  11","11  11"],
    ["11111 ","11  11","11111 ","11  11","11111 "],
    [" 1111 ","11  11","11    ","11  11"," 1111 "],
    ["1111  ","11  11","11  11","11  11","1111  "],
    ["111111","11    ","111111","11    ","111111"],
    ["111111","11    ","111111","11    ","11    "],
    [" 11111  ","11      ","11 1111 ","11 11 11"," 1111 11"],
    ["11  11","11  11","111111","11  11","11  11"],
    ["111111","  11  ","  11  ","  11  ","111111"],
    ["111111","   11 ","   11 ","11 11 ","11111 "],
    ["11  11","11 11 ","1111  ","11 11 ","11  11"],
    ["11    ","11    ","11    ","11    ","111111"],
    ["11   11","1111111","11 1 11","11   11","11   11"],
    ["11   11","111  11","1111 11","11 1111","11  111"],
    [" 1111 ","11  11","11  11","11  11"," 1111 "],
    ["11111 ","11  11","11111 ","11    ","11    "],
    [" 111111   ","11    11  ","11  1111  "," 1111111  ","        11"],
    ["111111","11  11","111111","11 11 ","11  11"],
    ["111111","11    ","111111","    11","111111"],
    ["111111","  11  ","  11  ","  11  ","  11  "],
    ["11  11","11  11","11  11","11  11","111111"],
    ["11    11","11    11"," 11  11 ","  1111  ","   11   "],
    ["11 11 11","11 11 11","11 11 11","11 11 11","11111111"],
    ["11  11"," 1111 ","  11  "," 1111 ","11  11"],
    ["11  11","11  11"," 1111 ","  11  ","  11  "],
    ["111111","   11 ","  11  "," 11   ","111111"],
    ["      ","      ","      ","      ","      "]]
    a2=[['a','A',0],['b','B',1],['c','C',2],['d','D',3],['e','E',4],['f','F',5],['g','G',6],
        ['h','H',7],['i','I',8],['j','J',9],['k','K',10],['l','L',11],['m','M',12],['n','N',13],
        ['o','O',14],['p','P',15],['q','Q',16],['r','R',17],['s','S',18],['t','T',19],['u','U',20],
        ['v','V',21],['w','W',22],['x','X',23],['y','Y',24],['z','Z',25],[" ","  ",26]]
    a3=[]
    a4=["","","","",""]
    alpha=input("Enter Your Name : ")
    choice=input("\n____________________\nMode Of Orientation\n____________________\n1)Vertical\n2)Horizontal\nYour Choice : ")
    print("____________________\n")
    leng=len(alpha)
    if choice=='1':
        for l in range(0,leng):
            for k in range(0,27):
                if alpha[l]==a2[k][0] or alpha[l]==a2[k][1]:
                    a3.append(a2[k][2])
        for i in range(0,len(a3)):
            for j in range(0,5):
                print(a1[a3[i]][j])
            print("\n")
    elif choice=='2':
        for l in range(0,leng):
            for k in range(0,27):
                if alpha[l]==a2[k][0] or alpha[l]==a2[k][1]:
                    a3.append(a2[k][2])
        for j in range(0,5):
            for i in range(0,len(a3)):
                a4[j]+=(a1[a3[i]][j])
                a4[j]+=" "
        ch=input("Enter Character In Output : ")
        print()
        for q in range(0,5):
            for w in range(0,len(a4[q])):
                a4[q] = a4[q].replace('1', ch)
        for m in range(0,5):
            print(a4[m])
    else:print("Invalid Choice...")
    print("___________________________")

def prh():
    global count
    print("======================================================")
    print("              MAED APPLICATIONS            ","Sl.no:",count)
    ch=int(input('''
------------------------------------------------------
1)Print Your Name
2)Calculator
3)Print Your Name Using Numbers\n___________________________
Enter Your Choice :'''))
    print("___________________________")
    if ch==1:
        printname()
    elif ch==2:
        calcu()
    elif ch==3:
        cap()
    else:
        print("Invalid Choice...")
        print("___________________________")
    cont()



count=1
attempt=1
login()
