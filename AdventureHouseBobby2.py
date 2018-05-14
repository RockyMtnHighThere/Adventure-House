"""
Initialize a global variable named ghost, to be used with 
the functions of program 134 on pages 299-300.
"""
#10.1 Optimize showRoom() method - modified by Bobby
#10.2 Add comments to pickRoom() - modified by Jess
#10.5 Add Underground rooms - modified by Trey
#10.7 Add a bomb in the dining room and use it in the underground passage - by Jess
#10.10 Add relevant sound as player enters room - modified by Bobby


ghost = 0
bomb = 0

def playGame():
  """ Prog 126 p 283: top-level function of adventure game """
  """ (this function is redefined below in program 133) """
  location = "Porch"
  showIntroduction()
  while not (location == "Exit") :
    showRoom(location)
    direction = requestString("Which direction?")
    location = pickRoom(direction, location)

def showIntroduction():
  """ Prog 127 p 284: showIntroduction for the adventure game """
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
    showPorch()
  if room == "Entryway":
    showEntryway()
  if room == "Kitchen":
    showKitchen()
  if room == "LivingRoom":
    showLR()
  if room == "DiningRoom":
    showDR()
 #Problem 10.5: Add Underground - Trey
  if room == "UndergroundPassage":
    showUGP()
  if room == "MassiveCavern":
    showMC()

# Problem 10.2: Add comments to pickRoom() - modified by Jess
def pickRoom(direction, room):
  """ Prog 129 p 284-285: pickRoom for the adventure game """
  """ (this function is redefined below in program 131) """
  
  # Allows user to quit or exit game
  if (direction == "quit") or (direction == "exit"):
    printNow("Goodbye!")
    return "Exit"
  
  # Provides user with game introduction
  if direction == "help":
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

# Problem

def showPorch():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  printNow("You are on the porch of a frightening looking house.")
  printNow("The windows are broken. It's a dark and stormy night.")
  printNow("You can go north into the house. If you dare.")
 # Problem 10.5: Add Underground - Trey
  printNow("Before you venture inside you see an underground tunnel to the east.")
 # 10.10: Add relevant sound as player enters room - Bobby ****Enter in pathway to sounds from ip-book/mediasources/yourfile.wav***
  sound = makeSound("users/dreamcanvas/desktop/ip-book/mediasources/croak.wav")
  play(sound)

def showEntryway():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  """ (this function is redefined below in program 134) """
  printNow("You are in the entry way of the house.")
  printNow("There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  printNow("There is a passageway to the north and another to the east.")
  printNow("The porch is behind you to the south.")

def showKitchen():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  """ (this function is redefined below in program 134) """
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
  printNow("You are in a living room.")
  printNow("There are couches, chairs, and small tables.")
  printNow("Everything is covered in dust and spider webs.")
  printNow("You hear a crashing noise in another room.")
  printNow("You can go north or west.")

def showDR():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  printNow("You are in the dining room.")
  printNow("There are remains of a meal on the table.")
  printNow("  You can't tell what it is,")
  printNow(" and maybe don't want to.")
  printNow("Was that a thump to the west?")
  printNow("You can go south or west")

# Problem 10.5: Add Underground rooms - modified by Trey
def showUGP():
  printNow("This underground tunnel seems to lead somewhere interesting.")
  printNow("It's big enough to crouch through so you walk with your phone's flashlight to light the path.")
  printNow("Without being able to see the end you think you've walked almost 100 yards.")
  printNow("The feelings of dread subside and you begin to sense a warmth the further you walk.")
  printNow("A soft glow of yellow light begins to appear. The other side of the tunnel, pehaps?")
  printNow("Do you want to continue east through the tunnel or go west, back to the Porch?")

def showMC():
  printNow("The light WAS the other side, but it's not outside!")
  printNow("When you were walking through the tunnel your feelings of dread subsided.")
  printNow("How could you have sensed this wonderful spring at the other end of the tunnel?")
  printNow("The spring smells fresh and if somehow giving off a golden glow.")
  printNow("You consider dipping your hand in it to test the temperature.")

def pickRoom(direction, room):
  """ program 131 pp 289-290: improved pickRoom for the adventure"""
  """ (replaces the previous definition of pickRoom, program 129)"""
  if (direction == "quit") or (direction == "exit"):
    printNow("Goodbye!")
    return "Exit"
  if direction == "help":
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
  printNow("You can't (or don't want to) go in that direction.")
  return room
  
#10.1 Optimize showRoom() method Bobby
def showRoom(room):
  """ Prog 132 p 296: improved showRoom for the adventure game"""
  """ (replaces previous definition of showRoom, program 128)"""
  printNow("===========")
  if room == "Porch":
    showPorch()
  elif room == "Entryway":
    showEntryway()
  elif room == "Kitchen":
    showKitchen()
  elif room == "LivingRoom":
    showLR()
  elif room == "DiningRoom":
    showDR()
 # Problem 10.5: Added two Underground rooms - Trey
  elif room == "UndergroundPassage":
    showUGP()
  elif room == "MassiveCavern":
    showMC()

def playGame():
  """ Prog 133 p 296: improved playGame for the adventure game"""
  """ (replaces previous definition of playGame, program 126)"""
  location = "Porch"
  showIntroduction()
  while not (location == "Exit") :
    showRoom(location)
    direction = requestString("Which direction?")
    printNow("You typed: "+direction)
    location = pickRoom(direction, location)

def showEntryway():
  """ Prog 134 pp 299-300: adding access to the ghost (global var)"""
  """ (replaces previous definition of showEntryway, program 130)"""
  """ (uses the global-scope variable ghost defined at the top)"""
  global ghost
  printNow("You are in the entry way of the house.")
  printNow(" There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  if ghost == 0:
    printNow("You suddenly feel cold.")
    printNow("You look up and see a thick mist.")
    printNow("It seems to be moaning.")
    printNow("Then it disappears.")
    ghost = 1
  printNow("There is a passageway to the north and another to the east.")
  printNow("The porch is behind you to the south.")

def showKitchen():
  """ Prog 134 pp 299-300: adding access to the ghost (global var)"""
  """ (replaces previous definition of showKitchen, program 130)"""
  """ (uses the global-scope variable ghost defined at the top)"""
  global ghost
  printNow("You are in the kitchen. ")
  printNow("All the surfaces are covered with pots,")
  printNow(" pans, food pieces, and pools of blood.")
  printNow("You think you hear something up the stairs") 
  printNow(" that go up the west side of the room.")
  printNow("It's a scraping noise, like something being dragged")
  printNow(" along the floor.")
  if ghost == 1:
    printNow("You see the mist you saw earlier.")
    printNow("But now it's darker, and red.")
    printNow("The moan increases in pitch and volume")
    printNow("  so now it sounds more like a yell!")
    printNow("Then it's gone.")
    ghost = 0
  printNow("You can go to the south or east.")
  
# Problem 10.7: Add a bomb in the dining room and use it in the underground passage - by Jess
def showDR():
  """ Problem 10.7 p 305: Add a bomb in the dining room) """
  """ (replaces previous definition of showDR, program 130) """
  """ (uses the global-scope variable bomb defined at the top)"""
  global bomb
  printNow("You are in the dining room.")
  printNow("There are remains of a meal on the table.")
  printNow("  You can't tell what it is,")
  printNow(" and maybe don't want to.")
  printNow("Was that a thump to the west?")
  if bomb == 0:
    printNow("You find a bomb on the dining room table.")
    printNow("Luckily, the Ogre is not in sight.")
    getBomb = requestString("Would you like to pickup the bomb: (yes/no)?")
    printNow("You typed: "+getBomb)
    if getBomb == "yes":
      printNow("Better hold onto the bomb in case you need it later.")
      bomb = 1
    else:
      printNow("You can go south or west")

# Problem 10.7: Add a bomb in the dining room and use it in the underground passage - by Jess
def showUGP():
  """ Problem 10.7 p 305: Use a bomb on the Orge) """
  """ (replaces previous definition of showUGP, added by Trey) """
  """ (uses the global-scope variable bomb defined at the top)"""
  global bomb
  play(silenceSound)
  printNow("This underground tunnel seems to lead somewhere interesting.")
  printNow("  It's big enough to crouch through so you walk with your phone's flashlight to light the path.")
  printNow("  Without being able to see the end you think you've walked almost 100 yards.")
  printNow("  The feelings of dread subside and you begin to sense a warmth the further you walk.")
  printNow("  A soft glow of yellow light begins to appear. The other side of the tunnel, pehaps?")
  printNow("Oh no, you see the Orge coming through the light at the end of the tunnel.")
  printNow("Better act fast, there's not much time.")
  if bomb == 1: # If you found the bomb in the dining room already
    useBomb = requestString("Do you want to use the bomb you found: (yes/no)?")
    printNow("You typed: "+useBomb)
    if useBomb == "yes":
      printNow("Great job. You slayed the Orge and may continue your adventure.")
      printNow("Do you want to continue east through the tunnel or go west, back to the Porch?")
      bomb = 0 # Reset bomb variable to allow it to be found in the dining room again
  else:
    printNow("  The Ogre's attention is caught by something else and he retreats.")
    printNow("He will be back, so you better prepare.")
# 10.10: Add relevant sound as player enters room - Bobby ****Enter in pathway to sounds from ip-book/mediasources/yourfile.wav***
  screamSound = makeSound("users/dreamcanvas/desktop/ip-book/mediasources/aah.wav")
  play(ScreamSound)