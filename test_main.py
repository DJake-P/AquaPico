import machine, time, onewire, ds18x20 
import InternetConnect, FileManagement, SensorLog

#Initial Setup
config = "config.json"
internetSettings = {}
roms = {}
start_time = time.time()
last_time = 0

#Sensors
temp_pin = machine.Pin(22)
temp_sensor = ds18x20.DS18X20(onewire.OneWire(temp_pin))

# Welcome Prompt
print("AquaPico")

# Setup Conditions
if FileManagement.FileExist(config) != True:
    # Create a new configuration file
    FileManagement.InitializeFileJ(config)

    # Getting internet connection details
    print("Getting Internet Connection Details:")
    internetSettings["SSID"] = input ("What is your SSID? ")
    internetSettings["PASS"] = input("What is your password? ")
    
    # Connect to the Internet
    InternetConnect.EstablishConnection(internetSettings["SSID"], internetSettings["PASS"])

    #Saving the internet settings in the config file
    FileManagement.AppendFileJ(config, "Wireless", internetSettings)

else:     
    # Retrieve saved Internet Details
    try: 
        ssid = FileManagement.FindSectionKeyValueJ(config, "Wireless", "SSID") 
        password = FileManagement.FindSectionKeyValueJ(config, "Wireless", "PASS")
    
        # Connect to the Internet
        InternetConnect.EstablishConnection(ssid, password)
    except:
        print("Improper Wireless Settings")


while True:
    
    poll_time = time.time() - start_time
    
    if poll_time >= 5:
        roms = SensorLog.SensorLog(temp_sensor)
        print(roms)
        start_time = time.time()
    
    
    
    
    
    
    
    
    