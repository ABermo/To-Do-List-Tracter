from datetime import datetime

items = {}

def help():
    print("Commands:")
    print("add <text>")
    print("update <id> <text>")
    print("mark <id> <text>")
    print("delete <id>")
    print("list")
    print("list <status>")
    print("create")
    print("\nUpdate changes description\nMark changes status")

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
    
def list_items(dic):
    for id, item in dic.items():
        print(f"{id}:")
        print(f"{item['description']}")
        print(f"{item['status']}")
        print(f"{item['createdAt']}")
        print(f"{item['updatedAt']}")
        print("\n")

def list_stat(dic, stat):
    for id, item in dic.items():
        if item['status'] == stat:
            print(f"{id}:")
            print(f"{item['description']}")
            print(f"{item['status']}")
            print(f"{item['createdAt']}")
            print(f"{item['updatedAt']}")
            print("\n")
            
while True:
    print("To Do List Tracker")
    print("Syntax:")
    print("<filename> <command> <id> <text>")
    print("Quit to exit")
    print("For more info enter Help")
    
    # Allows user to enter commands
    command = input("")
    
    # Exit Criteria
    if command.lower() == "quit": break
    if command.lower() == "help": 
        help()
        command = input("")
        if command.lower() == "quit": break    
        file = command.split(" ")[0]
    
    file = command.split(" ")[0]
    
    if (command.split(" ")[1].lower() == "create"):
        try:
            f = open(f"{file}.txt", "x")
        except:
            print("File already Exists")
            
    # Allows user to immediately use the file
    command = input("")
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
            elif len(command.split(" ")) > 2 and command.split(" ")[1].lower() == "list":
                list_stat(items, " ".join(command.split(" ")[2:]))
            elif task.lower() == "list":
                list_items(items)
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
            
