import time, os
import random

# variable
sistem_operasi = os.name
lists = ["batu", "gunting", "kertas"]

# utils
def clear():
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

# main
def inpuBot(item):
    randomIndex = random.randrange(len(item))
    return lists[randomIndex]

def inputUser(item):
    while(True):
        user = input("| gunting, batu, kertas (q)? ").lower()
        if (user in item):
            break
        elif (user == "q" or user == "exit"):
            exit()
        else:
            print("| output : input salah silakan coba lagi! \n")
            
    clear()
    return user

def render():
    print("\n=========================")
    print(f"| user \t: {user}   \t|")
    print("=========================")
    time.sleep(1)
    print(f"| bot \t: {bot}   \t|")
    print("=========================")
    time.sleep(1)

def play():
    if (user == bot):
        print("| hasil : kamu seri! \t|")
    elif (user == "gunting" and bot == "kertas" or user == "batu" and bot == "gunting") or user == "kertas" and bot == "batu":
        print("| hasil : kamu menang! \t|")
    else:
        print("| hasil : kamu kalah! \t|")

    print("=========================")


# setup
user = inputUser(lists)
bot = inpuBot(lists)
render()
play()