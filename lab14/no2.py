import os.path

filepath = input("Enter file path: ")
oldstr = input("Enter old string: ")
newstr = input("Enter new string: ")

def check_exists(filepath):
    if os.path.isfile(filepath):
        raise FileExistsError
    
    else:
        raise FileNotFoundError

def check_same_input(oldstr, newstr):
    if oldstr == newstr:
        raise ValueError

try :
    check_exists(filepath)
        
except FileNotFoundError:
    print("File is not exists")

except FileExistsError:
    
    try: 
        check_same_input(oldstr, newstr)
        file = open(filepath, "r")
        filedata = file.read()
        print(filedata)
        newfiledata = filedata.replace(oldstr, newstr)

        file = open(filepath, "w")
        file.write(newfiledata)
        file.close()
        print(newfiledata)
    
    except ValueError:
        print("Old string and new string are same")
    