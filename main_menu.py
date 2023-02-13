import sys
from edit_note import edit_note
from read_note import find_id_note, find_note_with_date, find_text_in_notes, find_title_note
from save_note import save_note

def main_menu():
    while True:
        print ('1 - save note')
        print ('2 - find and read note')
        print ('3 - edit note')
        print ('0 - exit')
        user_input = input ()
        
        match user_input:
            case "1":
                save_note()
            case "2":
                find_note_menu()
            case "3":
                edit_note()
            case "0":
                sys.exit()

def find_note_menu():
    print ('1 - find id note')
    print ('2 - find title of note')
    print ('3 - find text in notes')
    print ('4 - find note with date')
    print ('0 - exit to main menu')
    user_input = input ()
        
    match user_input:
        case "1":
            find_id_note()
        case "2":
            find_title_note()    
        case "3":
            find_text_in_notes()
        case "4":
            find_note_with_date()
        case "0":
            return         
            