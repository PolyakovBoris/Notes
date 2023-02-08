import sys
from save_note import save_note


def main_menu():
    while True:
        print ('1 - save note')
        print ('0 - exit')
        user_input = input ()
        
        match user_input:
            case "1":
                save_note()
            case "0":
                sys.exit()
            
            