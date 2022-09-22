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
        
def FindValueJ(filename, key, output=False):
    data = ReadFileJ(filename)
    for each in data:
       if each == key:
           if output == True:
               print(each + " : " + data[each])
           return True
           break
        
def AppendFileJ(filname, key, value):
    
    #If key doesn't exist, append to dictionary
    if FindValueJ(filename, key) != True:
        
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
        
        print("Append Failed: Key already exists. Only unquie keys allowed")

# Variables
filename = input("What file would you like to modify with extension (i.e. python.json)? ")
newKey = input ("What is the new key? ")
newValue = input("What is the new value for the key? ")

# Conditional file check
file_exist = ConfigExist(filename)

# Create a dummy file for testing
if file_exist == False:
    InitializeFileJ(filename)

# Read the json file and print the entire file
newData = ReadFileJ(filename)
print(newData)

FindValueJ(filename, "SSID", True)

# Append to dictionary
AppendFileJ(filename, newKey,newValue)

# Print new dictionary
newDic = ReadFileJ(filename)
print(newDic)
