import json
from save_note import save_note

def edit_note():
    user_input = ""
    while not user_input.isdigit():
        print ('input id of note for edit ->')
        user_input = input ()
    with open("data.json", "r") as file:       
        while True:
            line = file.readline()
            if not line:
                print("нет такого id")
                break
            data = json.loads(line)
            if (data['id'] == int(user_input)):
                print(data['note_title'])
                print(data['note'])
                save_note(data['id'])
