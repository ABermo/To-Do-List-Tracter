from datetime import datetime

id = 1
description = ""
status = ""
createdAt = ""
updatedAt = ""

items = {}



def add(id, dic, desc):
    dic[id] = {"description": desc, "status": "to do", "createdAt": datetime.now(), "updatedAt": False}

def update(id, dic, desc):
    dic[id]["description"] = desc
    dic[id]["updatedAt"] = datetime.now()

def mark(id, dic, stat):
    dic[id]["status"] = stat
    dic[id]["updatedAt"] = datetime.now()
    
def delete(id, dic):
    del dic[id]
    
    
while True:
    command = input("")
    
    if command.lower() == "quit": break
    
    file = command.split(" ")[0]
    
    try:
        with open(f"{file}.txt", "r") as f:
            for line in f:  
                sections = line.split(",")           
                items[id] = {"description": sections[0], "status": sections[1], "createdAt": sections[2], "updatedAt": sections[3]}
                id += 1
            
            task = command.split(" ")[1]
            
            if task.lower() == "add":
                add(command.split(" ")[2], items, command.split(" ")[3])
            elif task.lower() == "update":
                update(command.split(" ")[2], items, command.split(" ")[3])
            elif task.lower() == "mark":
                mark(command.split(" ")[2], items, command.split(" ")[3])
            elif task.lower() == "delete":
                delete(command.split(" ")[2], items)
        
        
            

    except FileNotFoundError:
        print("no file exists")
            
