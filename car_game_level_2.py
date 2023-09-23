# if start the it should show the car is start, again if the car is start than it showed the car is already started what are you doing
# similarly for stop massage

command = ""
started = False 
while True:
    command = input(">").lower()
    if command == "start" :
        if started :
            print("the car is already started..!!")
        else:
            started = True
            print("the car is started")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("car is stopped")
    elif command == "help":
        print("""
              Start - is to start the car
              Stop - is to stop the car
              Quit - is to quit the game
            """)
    elif command == quit:
        "break"
    else:
        ("sorry,i dont understand?")
        
        
    
            
        
