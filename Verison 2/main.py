import machine, time, onewire, ds18x20 
import InternetConnect, FileManagement, SensorLog

#Initial Setup
config = "config.json"
internetSettings = {}
settings_sec = "Settings"

#Logging Files
log_name = "sensor_data.json"
temp_sec = "Temperature"
level_sec = "Water_Level"


#Sensors
temp_pin = machine.Pin(22)
temp_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))

#Sensor Setups 
roms = {}

#Polling Variables
display_ST = time.time()
log_ST = time.time()
log_interval = 10 #in seconds

#last_time = 0

# Welcome Prompt
print("AquaPico")

# Setup Conditions
if FileManagement.FileExist(config) != True:
    # Create a new configuration file
    FileManagement.InitializeFileJ(config, True)

    # Getting internet connection details
    print("Getting Internet Connection Details:")
    internetSettings["SSID"] = input ("What is your SSID? ")
    internetSettings["PASS"] = input("What is your password? ")
    
    # Connect to the Internet
    InternetConnect.EstablishConnection(internetSettings["SSID"], internetSettings["PASS"])

    #Saving the internet settings in the config file
    FileManagement.AppendFileJ(config, "Settings", internetSettings)

else:     
    # Retrieve saved Internet Details
     try: 
        ssid = FileManagement.FindSectionKeyValueJ(config, "Settings", "SSID", True)
        paswd = FileManagement.FindSectionKeyValueJ(config, "Settings", "PASS", True)
        
        # Connect to the Internet
        InternetConnect.EstablishConnection(ssid, paswd)
     except:
         print("Improper Wireless Settings")
         
if FileManagement.FileExist(log_name) != True:
    FileManagement.InitializeFileJ(log_name, False)


#print(FileManagement.ReadFileJ(config))

while True:
    
    display_PT = time.time() - display_ST
    log_PT = time.time() - log_ST
    
    if display_PT >= 5:
        roms = SensorLog.SensorLog(temp_sensor, True)
        print(roms)
        
        display_ST = time.time()
    
    if log_PT >= log_interval:
        FileManagement.AppendFileJ(log_name, temp_sec, roms)
        
        log_PT = time.time()
    
    
    
    
    
    
    