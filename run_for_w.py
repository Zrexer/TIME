from datetime import datetime 
from os import system 
import pyfiglet
from time import sleep
from colorama import Fore as f 

system("cls")

while True: 
    time = datetime.now()
    print(f"{f.BLUE}_"*49)
    print(" ")
    print(time.strftime(f"{f.CYAN}TIME {f.RED}: "+f"{f.BLUE}[{f.YELLOW} %H {f.BLUE}: {f.YELLOW} %M {f.BLUE}: {f.YELLOW} %S {f.BLUE}]"))
    print(" ")
    print(f"{f.BLUE}_"*49)
    sleep(1)
    system("cls")
