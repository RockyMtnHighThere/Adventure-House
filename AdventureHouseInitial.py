""" Initialize a global variable named ghost, to be used with the
    functions of program 134 on pages 299-300."""
ghost = 0

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

def pickRoom(direction, room):
  """ Prog 129 p 284-285: pickRoom for the adventure game """
  """ (this function is redefined below in program 131) """
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

def showPorch():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  printNow("You are on the porch of a frightening looking house.")
  printNow("The windows are broken. It's a dark and stormy night.")
  printNow("You can go north into the house. If you dare.")

def showEntryway():
  """ Prog 130 p 284-285: showing rooms for the adventure game """
  """ (this function is redefined below in program 134) """
  printNow("You are in the entry way of the house.")
  printNow(" There are cobwebs in the corner.")
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
  printNow("You can't (or don't want to) go in that direction.")
  return room

def showRoom(room):
  """ Prog 132 p 296: improved showRoom for the adventure game"""
  """ (replaces previous definition of showRoom, program 128)"""
  printNow("===========")
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