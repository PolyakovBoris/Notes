import json
import datetime

def save_note (*num_id):
    with open("data.json", "r") as file:
        edit = False
        # определяем ID
        if (not num_id):
            if (sum(1 for line in open('data.json')) > 0):               
                data = json.loads(file.readlines() [-1])             
                num_id = data['id'] + 1
                print (num_id) 
            else:
                num_id = 1
        else:           
            edit = True
        note_title = (input ('введите заголовок заметки - '))
        note = (input ('введите текст заметки - '))
        mark = str(datetime.date.today())
        note_data = {}
        note_data = {'id': num_id, 'note_title' : note_title, 'note' : note, 'timemark' : mark}          
        if (edit == False):
            with open('data.json', 'a') as outfile:               
                json.dump(note_data, outfile, ensure_ascii=False)
                outfile.writelines('\n')
                print ("строка добавлена ")        
        else:           
            open('tmpdata.json', 'w').close()
            with open('data.json', 'r') as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    data = json.loads(line)  
                    if data['id'] != num_id:                                   
                        with open('tmpdata.json', 'a') as tmpfile:
                            json.dump(data, tmpfile, ensure_ascii=False)
                            tmpfile.writelines('\n')
                    else:
                        with open('tmpdata.json', 'a') as tmpfile:
                            json.dump(note_data, tmpfile, ensure_ascii=False)
                            tmpfile.writelines('\n')
            open('data.json', 'w').close()
            with open('tmpdata.json', 'r') as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    data = json.loads(line)                                   
                    with open('data.json', 'a') as newfile:
                        json.dump(data, newfile, ensure_ascii=False)
                        newfile.writelines('\n')          
    return
