import os
from commands import help
from commands import echo
from apps import calculator
from apps import game

def checker (cmdname):
    if cmdname == "help":
        help.run()
    if cmdname == "echo":
        echocmd = input("echo: ")
        echo.run(echocmd)
    if cmdname == "apps":
        print("[1] calculator")
        appselect = input("[ select number >")
        if appselect == "1" or 1:
            calculator.run()
    if cmdname == "clear":
        os.system('clear')

os.system('clear')
print("admin control panel running, start with [help] command.")
while True:
    cmdinput = input("AdminPanel> ")
    checker(cmdinput)
