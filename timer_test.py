from threading import Timer

def task(message):
    print(message)
    
timer = Timer(3, task, args=('Hello World',))

timer.start()

print("Waiting for the timer...")