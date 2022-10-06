#set the environment variable
#!/usr/bin/env python3

import os
import sys

# for colorized output
import colorama
from colorama import Fore, Back, Style

color = os.environ.get('COLOR')
meesage = os.environ.get('MESSAGE')
def main():
    #print the message with color
    if color == 'red':
        print(Fore.RED, meesage)
    elif color == 'green':
        print(Fore.GREEN , meesage)
    elif color == 'yellow':
        print(Fore.YELLOW , meesage)
    elif color == 'blue':
        print(Fore.BLUE , meesage)
    elif color == 'magenta':
        print(Fore.MAGENTA , meesage)
    elif color == 'cyan':
        print(Fore.CYAN , meesage)
    else:
        print("Evnironment variable COLOR and MESSAGE are not set, please set them and try again")
        print(Fore.CYAN, 'docker run -e COLOR=red  -e MESSAGE="Hello Nurse"  mmarzouq/python-automate:latest')
    
if __name__ == "__main__":
    main()
