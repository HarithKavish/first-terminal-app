from rich.console import Console
from rich.prompt import Confirm
from math import sqrt, pow, log, log10, log2
global console
import os

# from dotenv import dotenv_values
# temp = dotenv_values(".env")

console = Console()


def login():
    console.print(f"[green bold]Attempt {attempt}[/]")
    un = console.input("Username: ")
    pw = console.input("Password: ", password=True)
    # if un == temp["USERNAME"] and pw == temp["PASSWORD"]:
    # if un == os.environ["USERNAME"] and pw == os.environ["PASSWORD"]:
    if un == "admin" and pw == "admin":
        console.rule()
        console.log("Logged In ...")
        console.print("[green bold]Welcome Back[/]", justify="center")
        prh()
    else:
        console.print("[red bold]Username or Password is wrong.[/]")
        console.rule()
        login()


def continue_it():
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


def print_name():
    console.print("[bold]Print Your Name:[/]")
    i = input("Enter Your Name : ")
    console.print("Your Name       :", i)
    console.rule()


def calcu():
    console.print("[bold]Calculator:[/]")
    expression = str(console.input("Enter the expression: "))
    console.print(f"[bold]Answer: {eval(expression)}[/]")
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
    a2 = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25,
        " ": 26,
    }
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
            if alpha[l] in a2:
                a3.append(a2[k])
        for i in range(0, len(a3)):
            for j in range(0, 5):
                console.print(a1[a3[i]][j])
            console.print()
    elif choice == 2:
        for l in range(0, leng):
            if alpha[l] in a2:
                a3.append(a2[k])
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
    while True:
        console.rule()
        ch = int(ch)
        if ch == 1:
            print_name()
        elif ch == 2:
            calcu()
        elif ch == 3:
            cap()
        elif ch == 4:
            quit()
        else:
            console.print("Invalid Choice...")
            console.rule()
        continue_it()  


if __name__ == "__main__":
    global count, attempt
    count = 1
    attempt = 1
    login()
