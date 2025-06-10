import os,shutil

path = r"C:\Users\user\Desktop\Sorting pythonProject"
file = os.listdir(path)
print(file)

folder = ["pdf", "image", "sql"]

for i in range(0,3):
    folder_path = os.path.join(path,folder[i])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print(folder_path)

for files in file :
    if files.endswith(".pdf"):
        src = os.path.join(path,files)
        dst = os.path.join(path,"pdf",files)
        print("Moving",files)
        shutil.move(src,dst)

for files in file :
    if files.endswith(".jpg"):
        src = os.path.join(path,files)
        dst = os.path.join(path,"image",files)
        print("Moving",files)
        shutil.move(src,dst)

for files in file :
    if files.endswith(".sql"):
        src = os.path.join(path,files)
        dst = os.path.join(path,"sql",files)
        print("Moving",files)
        shutil.move(src,dst)
