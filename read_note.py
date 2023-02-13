import datetime
import json
    
#  ('1 - find id note')
def find_id_note():    
    print ('input id of note ->')
    user_input = input ()
    with open("data.json", "r") as file:       
        while True:
            line = file.readline()
            if not line:
                print("no such id")
                break
            print(line.strip())
            data = json.loads(line)
            print(data['id'])
            if (data['id'] == int(user_input)):
                print(data['note_title'])
                print(data['note'])
                print(data['timemark'])
                break
    
#  ('2 - find title note')
def find_title_note():    
    print ('input title of notes')
    user_input = input ()
    with open("data.json", "r") as file:       
        while True:
            line = file.readline()
            if not line:
                print("no such title ")
                break
            data = json.loads(line)
            if (str(data['note_title']).find(str(user_input)) == 0):
                print("user input ->" + user_input)
                print(data['note_title'])
                print(data['note'])
                print(data['timemark'])
                if (input ('1- continue find ') != '1'):
                    break
                print ("ищем в " + data['note_title'])
        print ('finding complete')
    
 #  ('3 - find text in notes') 
def find_text_in_notes():    
    print ('input text in notes')
    user_input = input ()
    with open("data.json", "r") as file:       
        while True:
            line = file.readline()
            if not line:
                print("no such text ")
                break
            data = json.loads(line)
            if (str(data['note']).find(str(user_input)) == 0):
                print("user input ->" + user_input)
                print(data['note_title'])
                print(data['note'])
                print(data['timemark'])
                if (input ('1- continue find or press any key ') != '1'):
                    break
                print ("ищем в " + data['note'])
        print ('finding complete')
    
#  ('4 - find note with date')
    
def find_note_with_date():    
    print ('input date of notes(..2023-02-09)')
    user_input = input ()
    with open("data.json", "r") as file:       
        while True:
            line = file.readline()
            if not line:
                print("no such date ")
                break
            data = json.loads(line)
            if (str(data['timemark']).find(str(user_input)) == 0):
                print("searching text ->" + user_input)
                print(data['note_title'])
                print(data['note'])
                print(data['timemark'])
                if (input ('1- continue find ') != '1'):
                    break
        print ('finding complete')

