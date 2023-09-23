start_game = input(">").lower()
if start_game == "start":
    print("> the car has started...")
elif start_game == "stop":
    print("> the car has been stop...")
elif start_game == "help":
    print(""" 
           start -Type start to start the car
           stop - Type stop to stop the car
           quit - Type to end the game""")
elif start_game == "quit":
    "break"
else:
    print("sorry, i don't understand..")

