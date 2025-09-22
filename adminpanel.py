print("admin controll panel running.")
from commands import help

def checker (cmdname):
    if cmdname == "help":
        help.run()

while True:
    cmdinput = input("AdminPanel> ")
    checker(cmdinput)