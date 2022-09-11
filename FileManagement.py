import json
import os


def FileExist(filename):
    try: 
        os.stat(filename)
        return True
    except:
        return False
    
def InitializeFileJ(filename):
    #Initial Configurations
    data = {"first_run": "True"}
    
    with open(filename, "w") as write_file:
        json.dump(data, write_file)
        
def ReadFileJ(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    return data
        
def FindKeyValueJ(filename, key, output=False):
    data = ReadFileJ(filename)
    for each in data:
       if each == key:
           if output == True:
               print(each + " : " + data[each])
           return True
           break

def ReturnKeyValueJ(filename, key, output=False):
    data = ReadFileJ(filename)
    for each in data:
       if each == key:
           if output != False:
               return "{" + each + ":" + data[each] + "}"
           return data[each]
           break
    return False

def AppendFileJ(filename, key, value):
    
    if FindKeyValueJ(filename, key) != True:
        
        with open(filename, "r+") as appendFile:
            
            #Convert/Load the json file into a python dictionary
            file_data = json.load(appendFile)
                
            #Add the new key/value pair to the dictionary in Python
            file_data[key] = value
                
            #Set the current position back to the beginning
            appendFile.seek(0)
                
            #Convert the file back to JSON
            json.dump(file_data, appendFile)
            
    else:
        
        print("Append Failed")
        