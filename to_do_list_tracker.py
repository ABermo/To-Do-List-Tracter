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
    # Allows user to enter commands
    command = input("")
    
    # Exit Criteria
    if command.lower() == "quit": break
    
    file = command.split(" ")[0]
    
    # Incase of invalid name
    try:
        with open(f"{file}.txt", "r") as f:
            for line in f:  
                
                # Check for empty lines
                line = line.strip()
                if not line:
                    continue
                    
                sections = line.split(",")      
                id = int(sections[0]) 
                # Convert into dictionary
                items[id] = {"description": sections[1], "status": sections[2], "createdAt": sections[3], "updatedAt": sections[4]}
                
            
            task = command.split(" ")[1]
            
            if task.lower() == "add":
                try:
                    id = max(items.keys()) + 1
                except:
                    id = 1
                add(id, items, command.split(" ")[2])
            else:
                # Incase they enter a non int for ID
                try:
                    id = int(command.split(" ")[2])
                except:
                    print("Invalid ID")
                    task = "null"
                
                # Incase of ID that does not exist
                try:
                    items[id] = items[id]
                except:
                    print("Invalid ID")
                    task = "null"
                
                
                if task.lower() == "update":
                    desc = " ".join(command.split(" ")[3:])
                    update(int(command.split(" ")[2]), items, desc)
                elif task.lower() == "mark":
                    stat = " ".join(command.split(" ")[3:])
                    mark(int(command.split(" ")[2]), items, stat)
                elif task.lower() == "delete":
                    delete(int(command.split(" ")[2]), items)
        
        with open(f"{file}.txt", "w") as f:
            for id, item in items.items():
                # Rewriting everything to the file
                f.write(f"{id},{item['description']},{item['status']},{item['createdAt']},{item['updatedAt']}\n")
        
            

    except FileNotFoundError:
        print("no file exists")
            
