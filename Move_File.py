import os
import shutil
from_dir="C:/Users/verma ji/Downloads"
to_dir="C:/Users/verma ji/Document_Files"
listof_files=os.listdir(from_dir)
#print(listof_files)

for file_name in  listof_files:
    name,ext=os.path.splitext(file_name)
    print(name)

    print(ext)
    if ext=="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"Document_files"
        path3=to_dir+"/"+"Document_files"+"/"+file_name
        print("path1",path1)
        print("path3",path3)
        if os.path.exists(path2): 
            print("moving "+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)   
            print("moving "+file_name+"...") 
            shutil.move(path1,path3)