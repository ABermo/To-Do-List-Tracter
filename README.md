# To-Do-List-Tracter
Python Program to manage to do tasks

# Usable
Enter command lines in the terminal, should be in the following format
<filename> <command> <id> <text>

Note that <id> and <text> are command specific, for information use the command Help

# How it works

```Python
file = command.split(" ")[0]
with open(f"{file}.txt", "r") as f:
```

The code splits the command based off spaces and takes the first item which should be the file name and attempts to open the text file

```Python
for line in f:  
  # Check for empty lines
  line = line.strip()
  if not line:
    continue
                    
  sections = line.split(",")      
  id = int(sections[0]) 
  # Convert into dictionary
  items[id] = {"description": sections[1], "status": sections[2], "createdAt": sections[3], "updatedAt": sections[4]}
```

It then reads through the full file and divides each line into a dictionary using the ID as the key

Once divided up into a dictionary, it is easy to edit, add or delete specific values it knows the ID

```Python
def update(id, dic, desc):
    dic[id]["description"] = desc
    dic[id]["updatedAt"] = datetime.now()
```

After the change has been created the code rewrites the file with the change

```Python
with open(f"{file}.txt", "w") as f:
  for id, item in items.items():
    # Rewriting everything to the file
    f.write(f"{id},{item['description']},{item['status']},{item['createdAt']},{item['updatedAt']}\n")
```

Editing the file after each change allows the user to more easily spot Errors they see and know what has or hasn't been changed
