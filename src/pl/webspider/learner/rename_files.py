import os

def rename_files():
    # (1) iterate all files names of dir, 'r' stands for rawpack
    file_list = os.listdir(r"E:\Training\Python\prank")
    print(file_list)
    cwd=os.getcwd()
    print (cwd)
    os.chdir(r"E:\Training\Python\prank")
    print (os.getcwd())
    # (2) rename file by file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()