""" Problem 10.3 Add Comments To All Methods - Joey"""

"""
Initialize a global variable named ghost, to be used with 
the functions of program 134 on pages 299-300.
"""
#10.1 Optimize showRoom() method - completed Bobby

ghost = 0

def playGame():
  """ Prog 126 p 283: top-level function of adventure game """
  """ (this function is redefined below in program 133) """
  location = "Porch"
  #display instructions for game - Joey
  showIntroduction()
  while not (location == "Exit") :
    #display description of current room - Joey
    showRoom(location)
    #get user's request (input) for a new direction - Joey
    direction = requestString("Which direction?")
    #allow user to pick new direction taking her to a new room - Joey
    location = pickRoom(direction, location)

def showIntroduction():
  """ Prog 127 p 284: showIntroduction for the adventure game """
  #display game information/instructions to user - Joey
  printNow("Welcome to the Adventure House!")
  printNow("In each room, you will be told")
  printNow(" which directions you can go.")
  printNow("You can move north, south, east, or west")
  printNow(" by typing that direction.")
  printNow("Type help to replay this introduction.")
  printNow("Type quit or exit to end the program.")

def showRoom(room):
  """ Prog 128 p 284: showRoom for the adventure game """
  """ (this function is redefined below in program 132) """
  if room == "Porch":
    #display porch description - Joey
    showPorch()
  if room == "Entryway":
    #display entry way description - Joey
    showEntryway()
  if room == "Kitchen":
    #display kitchen description - Joey
    showKitchen()
  if room == "LivingRoom":
    #display living room description - Joey
    showLR()
  if room == "DiningRoom":
    #display dining room description - Joey
    showDR()
  #Problem 10.5: Add Underground - Trey
  if room == "UndergroundPassage":
    #display underground passage description - Joey
    showUGP()
  if room == "MassiveCavern":
    #display massive cavern description - Joey
    showMC()

# Problem 10.2: Add comments to pickRoom() - modified by Jess
def pickRoom(direction, room):
  """ Prog 129 p 284-285: pickRoom for the adventure game """
  """ (this function is redefined below in program 131) """
  
  # Allows user to quit or exit game
  if (direction == "quit") or (direction == "exit"):
    #display this message when user exits or quits game
    printNow("Goodbye!")
    return "Exit"
  
  # Provides user with game introduction
  if direction == "help":
    #show instructions for game - Joey
    showIntroduction()
    return room
  
  # Problem 10.5: Add Underground - Trey
  #Check if the current room is "Porch"
  if room == "Porch":
    # if the desired direction is "north", the new room for the player is "Entryway"
    if direction == "north":
      return "Entryway"
    # if the desired direction is "east", the new room for the player is "Underground Passage"
    if direction == "east":
      return "UndergroundPassage"    
  
  # Check if the current room is "Underground Passage"
  if room == "UndergroundPassage":
    # if the desired direction is "east", the new room for the player is "Massive Cavern"
    if direction == "east":
      return "MassiveCavern"
  # if the desired direction is "west", send player back to "Porch"
    if direction == "west":
      return "Porch"
  
  # Check if the current room is "Massive Cavern"
  if room == "MassiveCavern":
    # if the desired direction is "west", send player back to "Underground Passage. Rooms stop at Massive Cavern. Please add more!
    if direction == "west":
      return "UndergroundPassage"    
  
  # Check if the current room is "Entryway"
  if room == "Entryway":
    # And if direction is "north", the new room for the player is "Kitchen"
    if direction == "north":
      return "Kitchen"
    # And if direction is "east", the new room for the player is "LivingRoom"
    if direction == "east":
      return "LivingRoom"
    # And if direction is "south", the new room for the player is "Porch"
    if direction == "south":
      return "Porch"
  
  # Check if the current room is "Kitchen"
  if room == "Kitchen":
    # And if direction is "east", the new room for the player is "DiningRoom"
    if direction == "east":
      return "DiningRoom"
    # And if direction is "south", the new room for the player is "Entryway"
    if direction == "south":
      return "Entryway"
  
  # Check if the current room is "LivingRoom"
  if room == "LivingRoom":
    # And if direction is "west", the new room for the player is "Entryway"
    if direction == "west":
      return "Entryway"
    # And if direction is "north", the new room for the player is "DiningRoom"
    if direction == "north":
      return "DiningRoom"
  
  # Check if the current room is "DiningRoom"
  if room == "DiningRoom":
    # And if direction is "west", the new room for the player is "Kitchen"
    if direction == "west":
      return "Kitchen"
    # And if direction is "south", the new room for the player is "LivingRoom"
    if direction == "south":
      return "LivingRoom"

def showPorch():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  #display description of porch - Joey
  printNow("You are on the porch of a frightening looking house.")
  printNow("The windows are broken. It's a dark and stormy night.")
  printNow("You can go north into the house. If you dare.")
  # Problem 10.5: Add Underground - Trey
  printNow("Before you venture inside you see an underground tunnel to the east.")

def showEntryway():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  """ (this function is redefined below in program 134) """
  #display description of entry way - Joey
  printNow("You are in the entry way of the house.")
  printNow(" There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  printNow("There is a passageway to the north and another to the east.")
  printNow("The porch is behind you to the south.")

def showKitchen():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  """ (this function is redefined below in program 134) """
  #display description of kitchen - Joey
  printNow("You are in the kitchen. ")
  printNow("All the surfaces are covered with pots,")
  printNow(" pans, food pieces, and pools of blood.")
  printNow("You think you hear something up the stairs") 
  printNow(" that go up the west side of the room.")
  printNow("It's a scraping noise, like something being dragged")
  printNow(" along the floor.")
  printNow("You can go to the south or east.")

def showLR():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  #display description of living room - Joey
  printNow("You are in a living room.")
  printNow("There are couches, chairs, and small tables.")
  printNow("Everything is covered in dust and spider webs.")
  printNow("You hear a crashing noise in another room.")
  printNow("You can go north or west.")

def showDR():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  #display description of dining room - Joey
  printNow("You are in the dining room.")
  printNow("There are remains of a meal on the table.")
  printNow("  You can't tell what it is,")
  printNow(" and maybe don't want to.")
  printNow("Was that a thump to the west?")
  printNow("You can go south or west")

  # Problem 10.5: Add Underground rooms - modified by Trey
def showUGP():
  #display description of underground tunnel - Joey
  printNow("This underground tunnel seems to lead somewhere interesting.")
  printNow("It's big enough to crouch through so you walk with your phone's flashlight to light the path.")
  printNow("Without being able to see the end you think you've walked almost 100 yards.")
  printNow("The feelings of dread subside and you begin to sense a warmth the further you walk.")
  printNow("A soft glow of yellow light begins to appear. The other side of the tunnel, pehaps?")
  printNow("Do you want to continue east through the tunnel or go west, back to the Porch?")

def showMC():
  #display description for massive cavern - Joey
  printNow("The light WAS the other side, but it's not outside!")
  printNow("When you were walking through the tunnel your feelings of dread subsided.")
  printNow("How could you have sensed this wonderful spring at the other end of the tunnel?")
  printNow("The spring smells fresh and if somehow giving off a golden glow.")
  printNow("You consider dipping your hand in it to test the temperature.")

def pickRoom(direction, room):
  """ program 131 pp 289-290: improved pickRoom for the adventure"""
  """ (replaces the previous definition of pickRoom, program 129)"""
  if (direction == "quit") or (direction == "exit"):
    #display this message if user exits game
    printNow("Goodbye!")
    return "Exit"
  if direction == "help":
    #display instructions for game - Joey
    showIntroduction()
    return room
  if room == "Porch":
    if direction == "north":
      return "Entryway"

  if room == "Entryway":
    if direction == "north":
      return "Kitchen"
    if direction == "east":
      return "LivingRoom"
    if direction == "south":
      return "Porch"
  if room == "Kitchen":
    if direction == "east":
      return "DiningRoom"
    if direction == "south":
      return "Entryway"
  if room == "LivingRoom":
    if direction == "west":
      return "Entryway"
    if direction == "north":
      return "DiningRoom"
  if room == "DiningRoom":
    if direction == "west":
      return "Kitchen"
    if direction == "south":
      return "LivingRoom"
# Problem 10.5: Add Underground rooms - Trey
  if room == "Porch":
    if direction == "north":
      return "Entryway"
    if direction == "east":
      return "UndergroundPassage" 
  if room == "UndergroundPassage":
    if direction == "east":
      return "MassiveCavern"
    if direction == "west":
      return "Porch"
  if room == "MassiveCavern":
    if direction == "west":
      return "UndergroundPassage"  
  #display cautionary message - Joey
  printNow("You can't (or don't want to) go in that direction.")
  return room
  
#10.1 Optimize showRoom() method Bobby
def showRoom(room):
  """ Prog 132 p 296: improved showRoom for the adventure game"""
  """ (replaces previous definition of showRoom, program 128)"""
  #display separator to appear between room descriptions - Joey
  printNow("===========")
  if room == "Porch":
    #display porch description - Joey
    showPorch()
  elif room == "Entryway":
    #display entry way description - Joey
    showEntryway()
  elif room == "Kitchen":
    #display kitchen description - Joey
    showKitchen()
  elif room == "LivingRoom":
    #display porch living description - Joey
    showLR()
  elif room == "DiningRoom":
    #display dining room description - Joey
    showDR()
  # Problem 10.5: Added two Underground rooms - Trey
  elif room == "UndergroundPassage":
    #display underground tunnel description- Joey
    showUGP()
  elif room == "MassiveCavern":
    #display massive cavern description- Joey
    showMC()

def playGame():
  """ Prog 133 p 296: improved playGame for the adventure game"""
  """ (replaces previous definition of playGame, program 126)"""
  location = "Porch"
  #display instructions for game - Joey
  showIntroduction()
  while not (location == "Exit") :
    #display description of current room - Joey
    showRoom(location)
    #get user's request (input) for a new direction - Joey
    direction = requestString("Which direction?")
    #display direction user typed - Joey
    printNow("You typed: "+direction)
    #allow user to pick new direction taking her to a new room - Joey
    location = pickRoom(direction, location)

def showEntryway():
  """ Prog 134 pp 299-300: adding access to the ghost (global var)"""
  """ (replaces previous definition of showEntryway, program 130)"""
  """ (uses the global-scope variable ghost defined at the top)"""
  global ghost
  #display description for entry way - Joey
  printNow("You are in the entry way of the house.")
  printNow(" There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  if ghost == 0:
    #display this description when user encounters a ghost in entry way - Joey
    printNow("You suddenly feel cold.")
    printNow("You look up and see a thick mist.")
    printNow("It seems to be moaning.")
    printNow("Then it disappears.")
    ghost = 1
  #display options for which direction user can go - Joey
  printNow("There is a passageway to the north and another to the east.")
  printNow("The porch is behind you to the south.")

def showKitchen():
  """ Prog 134 pp 299-300: adding access to the ghost (global var)"""
  """ (replaces previous definition of showKitchen, program 130)"""
  """ (uses the global-scope variable ghost defined at the top)"""
  global ghost
  #display description for kitchen - Joey
  printNow("You are in the kitchen. ")
  printNow("All the surfaces are covered with pots,")
  printNow(" pans, food pieces, and pools of blood.")
  printNow("You think you hear something up the stairs") 
  printNow(" that go up the west side of the room.")
  printNow("It's a scraping noise, like something being dragged")
  printNow(" along the floor.")
  if ghost == 1:
    #display this description when user encounters a ghost in kitchen - Joey
    printNow("You see the mist you saw earlier.")
    printNow("But now it's darker, and red.")
    printNow("The moan increases in pitch and volume")
    printNow("  so now it sounds more like a yell!")
    printNow("Then it's gone.")
    ghost = 0
  #display options for which direction user can go - Joey
  printNow("You can go to the south or east.")