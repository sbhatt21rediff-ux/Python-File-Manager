
import os
from pathlib import Path


def create_file():
    file_name=input("enter the name you want to keep for your file")
    p=Path(file_name)

    if not p.exists():
        with open(p,"w") as new_file:
            data=input("enter your content\n")
            new_file.write(data)
            print(f"file created succussfully and your content {data} has been saved.")

    else:
        print("this file already exists if you don't want to overwrite\nplease choose append option.")
        
def read_file():
    all_files_name=list(Path().glob("*")) 
    all_files=[]
    for i in all_files_name:
        if i.is_file():
            all_files.append(i)

    for a , items in enumerate(all_files):
        print(a,items)
    try:
        tell=int(input(f"enter number of file you want to read"))
        selected_file=all_files[tell]
        with open(selected_file,"r") as new_file:
            print("your file is here",new_file.read())
    except Exception as error:
        print("task failed")
def update_file():
    print("press 1 to update")
    print("press 2 to overwrite the content")
    print("press 3 to append")

    give=int(input("enter your response"))

    all_files_name=list(Path().glob("*")) 
    all_files=[]
    for i in all_files_name:
        if i.is_file():
            all_files.append(i)

    for a , items in enumerate(all_files):
        print(a,items)
    try:
        tell=int(input(f"enter number of file you want to update"))
        selected_file=all_files[tell]
        if give==1:
            old_content=input("write content you want to update")
            updated_content=input("write new content to be updated")

            with open(selected_file,"r") as new_file:
             c=new_file.read()
             d=c.replace(old_content,updated_content)
            with open(selected_file,"w") as new_file:
             new_file.write(d)
            print("Your content have been updated")
        elif give==2:
            with open(selected_file,"w") as new_file:
             new_data=input("enter your data here")
             new_file.write(new_data)
            print("Your content have been saved")
        elif give==3:
            with open(selected_file,"a") as new_file:
             newest_data=input("enter your data")
             new_file.write(newest_data)
            print("Your content have been added")
    except  Exception as error:
        print("task failed")

def delete_file():
    all_files_name=list(Path().glob("*")) 
    all_files=[]
    for i in all_files_name:
        if i.is_file():
            all_files.append(i)

    for a , items in enumerate(all_files):
        print(a,items)

    try:
            tell=int(input(f"enter number of file you want to delete"))
            selected_file=all_files[tell]
            os.remove(selected_file)
            print("task done, file removed")

    except Exception as error:
        print("Delete failed")



while True:
        print("1: Create | 2: Read | 3: Update | 4: Delete | 5: Exit")
        try:
            get = int(input("Enter choice: "))
            if get == 1: create_file()
            elif get == 2: read_file()
            elif get == 3: update_file()
            elif get == 4: delete_file()
            elif get == 5: 
                print("Goodbye!")
                break
            else: print("Choose 1-5.")
        except Exception as error:
            print("Please enter a number.")

