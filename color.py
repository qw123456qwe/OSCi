from colorama import Fore, Style

def print_line(text, type="normal"):
    if type == "start":
        print(Fore.GREEN + text + Style.RESET_ALL)

    elif type == "error":
        print(Fore.RED + text + Style.RESET_ALL)

    elif type == "keyword":
        print(Fore.CYAN + text + Style.RESET_ALL)

    else:
        print(text)
