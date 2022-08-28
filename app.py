from rich.console import Console
from rich.prompt import Confirm

global console
import os

from dotenv import load_dotenv

load_dotenv()
console = Console()


def login():
    console.print(f"[green bold]Attempt {attempt}[/]")
    un = console.input("Username: ")
    pw = console.input("Password: ", password=True)
    if un == os.environ["USERNAME"] and pw == os.environ["PASSWORD"]:
        console.rule()
        console.log("Logged In ...")
        console.print("[green bold]Welcome Back[/]", justify="center")
        prh()
    else:
        console.print("[red bold]Username or Password is wrong.[/]")
        console.rule()
        login()


def cont():
    if Confirm("Do you want to continue?"):
        global count
        count += 1
        prh()
    else:
        console.rule()
        if Confirm("Do You Want To Logout?"):
            console.rule()
            print("Logged Out ...")
            console.rule()
            if Confirm("Do you want to close?"):
                console.rule(characters="=")
                print("Maed Applications Closed...")
                console.rule(characters="=")
            if clos == 2:
                console.rule(characters="-")
                attempt += 1
                login()
        elif logout == 2:
            console.rule()
            clos = int(input("Do You Want To Close ?\n1)Yes\n2)No\nYour Choice : "))
            if clos == 1:
                console.rule(characters="=")
                console.print("Maed Applications Closed...")
                console.rule(characters="=")
            if clos == 2:
                console.rule(characters="-")
                attempt += 1
                login()


def printname():
    console.print("[bold]Print Your Name:[/]")
    i = input("Enter Your Name : ")
    console.print("Your Name       :", i)
    console.rule()


def calcu():
    console.print("[bold]Calculator:[/]]")
    calcu1 = int(input("Enter the 1st number : "))
    calcu2 = int(input("Enter the 2nd number : "))
    console.rule(characters="-")
    console.print("Sum        : ", calcu1 + calcu2)
    console.rule(characters="-")
    console.print("Difference : ", calcu1 - calcu2)
    console.rule(characters="-")
    console.print("Product    : ", calcu1 * calcu2)
    console.rule(characters="-")
    console.print("Quotient   : ", calcu1 / calcu2)
    console.rule()


def cap():
    console.print("[bold]Print Your Name:[/]")
    a1 = [
        [" 1111 ", "11  11", "111111", "11  11", "11  11"],
        ["11111 ", "11  11", "11111 ", "11  11", "11111 "],
        [" 1111 ", "11  11", "11    ", "11  11", " 1111 "],
        ["1111  ", "11  11", "11  11", "11  11", "1111  "],
        ["111111", "11    ", "111111", "11    ", "111111"],
        ["111111", "11    ", "111111", "11    ", "11    "],
        [" 11111  ", "11      ", "11 1111 ", "11 11 11", " 1111 11"],
        ["11  11", "11  11", "111111", "11  11", "11  11"],
        ["111111", "  11  ", "  11  ", "  11  ", "111111"],
        ["111111", "   11 ", "   11 ", "11 11 ", "11111 "],
        ["11  11", "11 11 ", "1111  ", "11 11 ", "11  11"],
        ["11    ", "11    ", "11    ", "11    ", "111111"],
        ["11   11", "1111111", "11 1 11", "11   11", "11   11"],
        ["11   11", "111  11", "1111 11", "11 1111", "11  111"],
        [" 1111 ", "11  11", "11  11", "11  11", " 1111 "],
        ["11111 ", "11  11", "11111 ", "11    ", "11    "],
        [" 111111   ", "11    11  ", "11  1111  ", " 1111111  ", "        11"],
        ["111111", "11  11", "111111", "11 11 ", "11  11"],
        ["111111", "11    ", "111111", "    11", "111111"],
        ["111111", "  11  ", "  11  ", "  11  ", "  11  "],
        ["11  11", "11  11", "11  11", "11  11", "111111"],
        ["11    11", "11    11", " 11  11 ", "  1111  ", "   11   "],
        ["11 11 11", "11 11 11", "11 11 11", "11 11 11", "11111111"],
        ["11  11", " 1111 ", "  11  ", " 1111 ", "11  11"],
        ["11  11", "11  11", " 1111 ", "  11  ", "  11  "],
        ["111111", "   11 ", "  11  ", " 11   ", "111111"],
        ["      ", "      ", "      ", "      ", "      "],
    ]
    a2 = [
        ["a", "A", 0],
        ["b", "B", 1],
        ["c", "C", 2],
        ["d", "D", 3],
        ["e", "E", 4],
        ["f", "F", 5],
        ["g", "G", 6],
        ["h", "H", 7],
        ["i", "I", 8],
        ["j", "J", 9],
        ["k", "K", 10],
        ["l", "L", 11],
        ["m", "M", 12],
        ["n", "N", 13],
        ["o", "O", 14],
        ["p", "P", 15],
        ["q", "Q", 16],
        ["r", "R", 17],
        ["s", "S", 18],
        ["t", "T", 19],
        ["u", "U", 20],
        ["v", "V", 21],
        ["w", "W", 22],
        ["x", "X", 23],
        ["y", "Y", 24],
        ["z", "Z", 25],
        [" ", "  ", 26],
    ]
    a3 = []
    a4 = ["", "", "", "", ""]
    alpha = console.input("Enter Your Name : ")
    choice = int(
        console.input(
            "Mode Of Orientation:\n\t1) Vertical\n\t2) Horizontal\nYour Choice:"
        )
    )
    console.rule()
    leng = len(alpha)
    if choice == 1:
        for l in range(0, leng):
            for k in range(0, 27):
                if alpha[l] == a2[k][0] or alpha[l] == a2[k][1]:
                    a3.append(a2[k][2])
        for i in range(0, len(a3)):
            for j in range(0, 5):
                console.print(a1[a3[i]][j])
            console.print()
    elif choice == 2:
        for l in range(0, leng):
            for k in range(0, 27):
                if alpha[l] == a2[k][0] or alpha[l] == a2[k][1]:
                    a3.append(a2[k][2])
        for j in range(0, 5):
            for i in range(0, len(a3)):
                a4[j] += a1[a3[i]][j]
                a4[j] += " "
        for m in range(0, 5):
            console.print(a4[m])
    else:
        console.print("Invalid Choice...")
    console.rule()


def prh():
    global count
    console.rule()
    console.print(f"MAED APPLICATIONS Sl.no: {count}", justify="center")
    console.rule()
    ch = console.input(
        """[b]Menu:[/]
1) Print Your Name
2) Calculator
3) Print Your Name Using Numbers
4) Quit
Enter Your Choice: """
    )
    console.rule()
    ch = int(ch)
    if ch == 1:
        printname()
    elif ch == 2:
        calcu()
    elif ch == 3:
        cap()
    elif ch == 4:
        quit()
    else:
        console.print("Invalid Choice...")
        console.rule()
    cont()


if __name__ == "__main__":
    global count, attempt
    count = 1
    attempt = 1
    login()
