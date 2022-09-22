import json
import os

class FileManage:

    def __init__(self, filename, data = {}) -> None:
        self.filename = filename
        self.data = data
        
    @staticmethod
    def FileExist(filename):
        try: 
            os.stat(filename)
            return True
        except:
            return False
    
    def InitializeFileJ(self):
        #Initial Configuration
        with open(self.filename, "w") as write_file:
            json.dump(self.data, write_file)
            
    def ReadFileJ(self):
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)
        return data
            
    def FindKeyValueJ(self, key, output=False):
        data = self.ReadFileJ()
        for each in data:
            if each == key:
                if output == True:
                    print(each + " : " + data[each])
                return True
                break

    def ReturnKeyValueJ(self, key, output=False):
        data = self.ReadFileJ(self.filename)
        for each in data:
            if each == key:
                if output != False:
                    return "{" + each + ":" + data[each] + "}"
                return data[each]
                break
            return False

    def AppendFileJ(self, data):
        
        for key in data: 
            if self.FindKeyValueJ(self.filename, key) != True:
                
                with open(self.filename, "r+") as appendFile:
                    
                    #Convert/Load the json file into a python dictionary
                    file_data = json.load(appendFile)
                        
                    #Add the new key/value pair to the dictionary in Python
                    file_data[key] = data[key]
                        
                    #Set the current position back to the beginning
                    appendFile.seek(0)
                        
                    #Convert the file back to JSON
                    json.dump(file_data, appendFile)
                    
            else:
                
                print("Append Failed")
    
    def UpdateKeyValueJ(self, data):
        
        for key in data:
            if self.FindKeyValueJ(self.filename, key) != False:
                
                with open(self.filename, "r+") as appendFile:
                    
                    #Convert/Load the json file into a python dictionary
                    file_data = json.load(appendFile)
                        
                    #Add the new key/value pair to the dictionary in Python
                    file_data.update(data)
                        
                    #Set the current position back to the beginning
                    appendFile.seek(0)
                        
                    #Convert the file back to JSON
                    json.dump(file_data, appendFile)
                    
            else:
                
                print("Update Failed")

data = {"first_run": "True"}
append = {"Test": "True"}
update = {"first_run":"False", "Test":"False"}
config = FileManage("config", data )
config.InitializeFileJ()
print(config.ReadFileJ())
print("\n")
config.AppendFileJ(append)
print(config.ReadFileJ())
config.UpdateKeyValueJ(update)
config.FindKeyValueJ("first_run", True)
print(config.ReadFileJ())
