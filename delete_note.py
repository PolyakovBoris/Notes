import json

def delete_note():
    user_input = ""
    while not user_input.isdigit():
        print ('input id of note for delete (must be integer) ->')
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
                break
    open('tmpdata.json', 'w').close()
    with open('data.json', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = json.loads(line)

            if data['id'] != int(user_input):                                   
                with open('tmpdata.json', 'a') as tmpfile:
                    json.dump(data, tmpfile, ensure_ascii=False)
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
                