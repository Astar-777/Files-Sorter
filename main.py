import os
import shutil
from sys import exit

folders={
    'videos':['.mp4', '.mkv'],
    'audios':['.mp3', '.wav'],
    'images':['.jpeg', '.jpg', '.png', '.gif'],
    'documents':['.doc', '.xlsx', '.xls', '.pdf', '.txt', '.json'],
    'archives':['.zip', '.rar'],
    'applications':['.exe', '.msi']
}


def create_and_move(ext, file_name):
    find = False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory, folder_name))
            shutil.move(os.path.join(directory, file_name), os.path.join(directory, folder_name))
            find = True
            break

    if find == False:
        if "others" not in os.listdir(directory):
            os.mkdir(os.path.join(directory, "others"))
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, "others"))

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder)) == True:
            os.rename(os.path.join(directory, folder), os.path.join(directory, folder.lower()))

directory = input("Enter the location: ")
rename_folder()
all_files = os.listdir(directory)

length = len(all_files)
count = 1

for i in all_files:
    if os.path.isfile(os.path.join(directory,i)) == True:
        create_and_move(i.split(".")[-1], i)
        print(f"Total Files: {length} | Sorted: {count} | Left: {length-count}")
    count += 1

print("Sorted all the files!")
input("\nPress enter to exit!")
exit()