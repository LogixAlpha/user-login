from colorama import Back , Fore , Style , init
init(autoreset=True)

print(f"{Back.LIGHTCYAN_EX} Welcome to Simple Login User! ".center(10))
print(f"{Fore.LIGHTBLACK_EX} This project is Uncompleted! ".center(10))

print(
    f"1- {Fore.GREEN+Style.BRIGHT}Sign in {Style.RESET_ALL}\n"
    f"2- {Fore.BLUE+Style.BRIGHT}Login in [soon] {Style.RESET_ALL}\n"
)
choice = input(f"{Back.LIGHTMAGENTA_EX+Style.DIM}Your Choice :{Style.RESET_ALL}")
choice = int(choice)
def script():
    if choice == 1 :
        username = input(f"{Back.LIGHTBLACK_EX+Style.BRIGHT}Enter your username:{Style.RESET_ALL}")
        if len(username) <= 2 :
            print(f'{Style.BRIGHT+Fore.RED}3 characters or more required!{Style.RESET_ALL}')
            script()
        else:
            password = input(f"{Back.LIGHTBLACK_EX+Style.BRIGHT}Enter your password:{Style.RESET_ALL}")
            if len(password) == 0 :
                print(f"{Style.DIM}Welcome{Style.RESET_ALL} {Fore.MAGENTA+Style.BRIGHT}{username}{Style.RESET_ALL}! \n"
                      f"{Fore.LIGHTRED_EX+Style.DIM}You didn't set any password!{Style.RESET_ALL} \n")    
script()               