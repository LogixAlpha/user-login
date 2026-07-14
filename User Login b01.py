from colorama import Back , Fore , Style , init
import time
init(autoreset=True)

print(f"{Back.LIGHTCYAN_EX} Welcome to Simple Login User! ".center(10))
time.sleep(1)
print(f"{Fore.LIGHTBLACK_EX} This project is Uncompleted! ".center(10))
time.sleep(1.5)
print(
    f"1- {Fore.GREEN+Style.BRIGHT}Sign in {Style.RESET_ALL}\n"
    f"2- {Fore.BLUE+Style.BRIGHT}Login in (soon) {Style.RESET_ALL}\n"
)
choice = input(f"{Style.RESET_ALL+Back.LIGHTMAGENTA_EX+Style.DIM}Your Choice :{Style.RESET_ALL}")
choice = int(choice)
def script():
    if choice == 1 :
        username = input(f"{Style.RESET_ALL+Back.LIGHTBLACK_EX+Style.BRIGHT}Enter your username:{Style.RESET_ALL+Fore.LIGHTBLUE_EX+Style.BRIGHT}")
        if len(username) <= 2 :
            time.sleep(1)
            print(f'{Style.RESET_ALL+Style.BRIGHT+Fore.RED}3 characters or more required!{Style.RESET_ALL}')
            time.sleep(0.5)
            script()
        else:
            password = input(f"{Style.RESET_ALL+Back.LIGHTBLACK_EX+Style.BRIGHT}Enter your password:{Style.RESET_ALL+Fore.LIGHTBLUE_EX+Style.BRIGHT}")
            if len(password) == 0 :
                print(f"{Style.RESET_ALL+Style.DIM}Welcome{Style.RESET_ALL} {Fore.MAGENTA+Style.BRIGHT}{username}{Style.RESET_ALL}! \n"
                      f"{Style.RESET_ALL+Fore.LIGHTRED_EX+Style.DIM}You didn't set any password!{Style.RESET_ALL} \n")   
            elif len(password) <= 3:
                time.sleep(.75)
                print(f'{Style.RESET_ALL+Style.BRIGHT+Fore.RED}4 characters or more required!{Style.RESET_ALL}')   
                time.sleep(.5)
                script()
            else :
                time.sleep(.7)
                print(f"{Style.RESET_ALL+Style.DIM}Welcome{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX+Style.BRIGHT}{username}{Style.RESET_ALL}! \n"
                      f"{Style.RESET_ALL+Style.DIM}Your password is:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX+Style.BRIGHT}{password}{Style.RESET_ALL} \n")    

    elif choice == 2 :
    else:
        time.sleep()
        








script()               
