import json

def save_note ():
    note_title = (input ('введите заголовок заметки'))
    note = (input ('введите заметку'))
    data = {note_title: note}

    with open('data.txt', 'a') as outfile:
        outfile.write("\n")
        json.dump(data, outfile, separators=("", ":"))
        
    return