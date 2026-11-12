id = 0
description = ""
status = ""
createdAt = ""
updatedAt = ""

items = {}

while True:
    command = input("")
    
    if command.lower() == "quit": break
    
    file = command.split(" ")[0]
    
    try:
        with open(f"{file}.txt", "r") as f:
            print("success")

    except FileNotFoundError:
        print("no file exists")
            
        