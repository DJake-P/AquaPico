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
    data = {"Settings":
            
            {'first_run': 'True'}
            
            }
    
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
               print(data[each]) 
           return True
           break
        
def FindSectionKeyValueJ (filename, section, key, output=False):
    data = ReadFileJ(filename)
    for each in data[section]:
        if each == key:
            if output == True:
                print(each)
            return True
            break

def ReturnKeyValueJ(filename, key, output=False):
    data = ReadFileJ(filename)
    for each in data:
        dic = {}
        dic[each] = data[each]
        if each == key:
           if output != False:
               return print(dic[each])
           return dic[each]
           break
    return False

def AppendFileJ(filename, section, newData):
    
    for each in newData:
        dic = {}
        dic[each] = newData[each]

        with open(filename, "r+") as appendFile:
            
            #Convert/Load the json file into a python dictionary
            file_data = json.load(appendFile)
            
            if not ReturnKeyValueJ(filename, section):
                file_data[section] = {}
                
            #Add the new key/value pair to the dictionary in Python
            file_data[section].update(dic)
       
            #Set the current position back to the beginning
            appendFile.seek(0)
                
            #Convert the file back to JSON
            json.dump(file_data, appendFile)   
        
## Test Code
filename = "test.json"
section = "Who"
key = "test"
newData = {"Jake":"Porter", "test":"Porter"}


if not FileExist(filename):
    InitializeFileJ(filename)

#FindSectionKeyValueJ(filename, section, key)
#FindKeyValueJ(filename, section)

AppendFileJ(filename, section, newData)

ReturnKeyValueJ(filename, section, True)
print(ReadFileJ(filename))