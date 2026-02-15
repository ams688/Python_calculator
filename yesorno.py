import practice

print("\033[1mWelcome!\033[0m")
yesorno = input("Do you want to start the calculator (yes/no):  ")

if yesorno == "no":
    print("you have exited the program")
else:
    if yesorno == "yes":
        practice.Calculator()