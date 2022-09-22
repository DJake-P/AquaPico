import network, utime

def EstablishConnection (ssid, password):
    max_attempt = 10
    while max_attempt > 0: 

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        # Wait for connect or fail
        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('Waiting for connection...')
            utime.sleep(1)

        #Error Handling
        if wlan.status() !=3:
            print('Connection Failed')
            max_attempt -= 1
        else:
            print('Connected')
            status = wlan.ifconfig()
            print("IP: " + status[0])
            
            #break the loop
            break