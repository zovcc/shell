#!/usr/bin/env python3

import pyautogui
import time
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from gi.repository import Gtk

class bcolors:
    PASS = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    
print("")
testsPassed = 0
testsFailed = 0

def getAllWindows():
  time.sleep(0.5)
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while Gtk.events_pending():
    Gtk.main_iteration()
  time.sleep(0.5)
  return screen.get_windows()

def getActiveWindow():
  time.sleep(0.5)
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while Gtk.events_pending():
    Gtk.main_iteration()
  time.sleep(0.5)
  return screen.get_active_window()

def getActiveWindowName():
  time.sleep(0.5)
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while Gtk.events_pending():
    Gtk.main_iteration()
  time.sleep(0.5)
  return screen.get_active_window().get_application().get_name()
  # return screen.get_active_window().get_name()
  
def getScreenDimensions():
  screen = Wnck.Screen.get_default()
  screen.force_update()
  screenWidth = screen.get_width()
  screenHeight = screen.get_height()
  screenDimensions = [screenWidth, screenHeight]
  return screenDimensions

def increaseWidth():
  global testsPassed
  global testsFailed
  pyautogui.hotkey('winleft', 'enter')
  oldWidth = getActiveWindow().get_geometry()[2]
  oldHeight = getActiveWindow().get_geometry()[3]
  # print("Old window dimensions: " + str(oldWidth) + " by " + str(oldHeight))
  time.sleep(0.25)
  pyautogui.hotkey('shiftleft', 'right')
  time.sleep(0.25)
  pyautogui.hotkey('enter')
  newWidth = getActiveWindow().get_geometry()[2]
  newHeight = getActiveWindow().get_geometry()[3]
  # print("New window dimensions: " + str(newWidth) + " by " + str(newHeight))
  if newWidth > oldWidth:
    print(bcolors.PASS + "PASS:" + bcolors.ENDC + " Shift-Right increased window size.")
    testsPassed += 1
  elif newWidth < oldWidth:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Right should have increased window size, but it decreased instead.")
    testsFailed += 1
  elif newWidth == oldWidth:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Right did not change window size.")
    testsFailed += 1

def increaseHeight():
  global testsPassed
  global testsFailed
  pyautogui.hotkey('winleft', 'enter')
  oldWidth = getActiveWindow().get_geometry()[2]
  oldHeight = getActiveWindow().get_geometry()[3]
  # print("Old window dimensions: " + str(oldWidth) + " by " + str(oldHeight))
  time.sleep(0.25)
  pyautogui.hotkey('shiftleft', 'down')
  time.sleep(0.25)
  pyautogui.hotkey('enter')
  newWidth = getActiveWindow().get_geometry()[2]
  newHeight = getActiveWindow().get_geometry()[3]
  # print("New window dimensions: " + str(newWidth) + " by " + str(newHeight))
  if newHeight > oldHeight:
    print(bcolors.PASS + "PASS:" + bcolors.ENDC + " Shift-Down increased window size.")
    testsPassed += 1
  elif newHeight < oldHeight:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Down should have increased window size, but it decreased instead.")
    testsFailed += 1
  elif newHeight == oldHeight:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Down did not change window size.")
    testsFailed += 1

def decreaseWidth():
  global testsPassed
  global testsFailed
  pyautogui.hotkey('winleft', 'enter')
  oldWidth = getActiveWindow().get_geometry()[2]
  oldHeight = getActiveWindow().get_geometry()[3]
  # print("Old window dimensions: " + str(oldWidth) + " by " + str(oldHeight))
  time.sleep(0.25)
  pyautogui.hotkey('shiftleft', 'left')
  time.sleep(0.25)
  pyautogui.hotkey('enter')
  newWidth = getActiveWindow().get_geometry()[2]
  newHeight = getActiveWindow().get_geometry()[3]
  # print("New window dimensions: " + str(newWidth) + " by " + str(newHeight))
  if newWidth < oldWidth:
    print(bcolors.PASS + "PASS:" + bcolors.ENDC + " Shift-Left decreased window size.")
    testsPassed += 1
  elif newWidth > oldWidth:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Left should have decreased window size, but it increased instead.")
    testsFailed += 1
  elif newWidth == oldWidth:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Left did not change window size.")
    testsFailed += 1

def decreaseHeight():
  global testsPassed
  global testsFailed
  pyautogui.hotkey('winleft', 'enter')
  oldWidth = getActiveWindow().get_geometry()[2]
  oldHeight = getActiveWindow().get_geometry()[3]
  # print("Old window dimensions: " + str(oldWidth) + " by " + str(oldHeight))
  time.sleep(0.25)
  pyautogui.hotkey('shiftleft', 'up')
  time.sleep(0.25)
  pyautogui.hotkey('enter')
  newWidth = getActiveWindow().get_geometry()[2]
  newHeight = getActiveWindow().get_geometry()[3]
  # print("New window dimensions: " + str(newWidth) + " by " + str(newHeight))
  if newHeight < oldHeight:
    print(bcolors.PASS + "PASS:" + bcolors.ENDC + " Shift-Up decreased window size.")
    testsPassed += 1
  elif newHeight > oldHeight:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Up should have decreased window size, but it increased instead.")
    testsFailed += 1
  elif newHeight == oldHeight:
    print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " Shift-Up did not change window size.")
    testsFailed += 1

# TEST ITEM: Super + direction keys changes focus in the correct direction
# start with focus at bottom right
pyautogui.hotkey('winleft', 'right')
pyautogui.hotkey('winleft', 'down')

# First, get a list of open windows and figure out each window's position.
allWindows = getAllWindows()
for i in allWindows:
  print("Window " + str(allWindows.index(i)))
  print("Application: " + i.get_application().get_name())
  # print("Title: " + i.get_name())
  print("Geometry: " + str(i.get_geometry()))
  print("")
  
# Get the dimensions of the screen.
print("Screen dimensions: " + str(getScreenDimensions()))
print("")

# This will only work if there are exactly 4 windows.
if len(allWindows) == 4:
  print("There are 4 windows.")
  
  topLeft = None
  bottomLeft = None
  topRight = None
  bottomRight = None
  
  # Find out where Window 0 is.
  if allWindows[0].get_geometry()[0] < allWindows[1].get_geometry()[0] or allWindows[0].get_geometry()[0] < allWindows[2].get_geometry()[0] or allWindows[0].get_geometry()[0] < allWindows[3].get_geometry()[0]:
    # Window 0 is on the left.
    if allWindows[0].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[0].get_geometry()[1] < allWindows[2].get_geometry()[1] or allWindows[0].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topLeft = allWindows[0]
      print(str(topLeft.get_application().get_name()) + " is in the top left.")
    elif allWindows[0].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[0].get_geometry()[1] > allWindows[2].get_geometry()[1] or allWindows[0].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomLeft = allWindows[0]
      print(str(bottomLeft.get_application().get_name()) + " is in the bottom left.")
  elif allWindows[0].get_geometry()[0] > allWindows[1].get_geometry()[0] or allWindows[0].get_geometry()[0] > allWindows[2].get_geometry()[0] or allWindows[0].get_geometry()[0] > allWindows[3].get_geometry()[0]:
    # Window 0 is on the right.
    if allWindows[0].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[0].get_geometry()[1] < allWindows[2].get_geometry()[1] or allWindows[0].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topRight = allWindows[0]
      print(str(topRight.get_application().get_name()) + " is in the top right.")
    elif allWindows[0].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[0].get_geometry()[1] > allWindows[2].get_geometry()[1] or allWindows[0].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomRight = allWindows[0]
      print(str(bottomRight.get_application().get_name()) + " is in the bottom right.")

  # Find out where Window 1 is.
  if allWindows[1].get_geometry()[0] < allWindows[0].get_geometry()[0] or allWindows[1].get_geometry()[0] < allWindows[2].get_geometry()[0] or allWindows[1].get_geometry()[0] < allWindows[3].get_geometry()[0]:
    # Window 1 is on the left.
    if allWindows[1].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[1].get_geometry()[1] < allWindows[2].get_geometry()[1] or allWindows[1].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topLeft = allWindows[1]
      print(str(topLeft.get_application().get_name()) + " is in the top left.")
    elif allWindows[1].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[1].get_geometry()[1] > allWindows[2].get_geometry()[1] or allWindows[1].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomLeft = allWindows[1]
      print(str(bottomLeft.get_application().get_name()) + " is in the bottom left.")
  elif allWindows[1].get_geometry()[0] > allWindows[0].get_geometry()[0] or allWindows[1].get_geometry()[0] > allWindows[2].get_geometry()[0] or allWindows[1].get_geometry()[0] > allWindows[3].get_geometry()[0]:
    # Window 1 is on the right.
    if allWindows[1].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[1].get_geometry()[1] < allWindows[2].get_geometry()[1] or allWindows[1].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topRight = allWindows[1]
      print(str(topRight.get_application().get_name()) + " is in the top right.")
    elif allWindows[1].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[1].get_geometry()[1] > allWindows[2].get_geometry()[1] or allWindows[1].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomRight = allWindows[1]
      print(str(bottomRight.get_application().get_name()) + " is in the bottom right.")
      
  # Find out where Window 2 is.
  if allWindows[2].get_geometry()[0] < allWindows[0].get_geometry()[0] or allWindows[2].get_geometry()[0] < allWindows[1].get_geometry()[0] or allWindows[2].get_geometry()[0] < allWindows[3].get_geometry()[0]:
    # Window 2 is on the left.
    if allWindows[2].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[2].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[2].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topLeft = allWindows[2]
      print(str(topLeft.get_application().get_name()) + " is in the top left.")
    elif allWindows[2].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[2].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[2].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomLeft = allWindows[2]
      print(str(bottomLeft.get_application().get_name()) + " is in the bottom left.")
  elif allWindows[2].get_geometry()[0] > allWindows[0].get_geometry()[0] or allWindows[2].get_geometry()[0] > allWindows[1].get_geometry()[0] or allWindows[2].get_geometry()[0] > allWindows[3].get_geometry()[0]:
    # Window 2 is on the right.
    if allWindows[2].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[2].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[2].get_geometry()[1] < allWindows[3].get_geometry()[1]:
      topRight = allWindows[2]
      print(str(topRight.get_application().get_name()) + " is in the top right.")
    elif allWindows[2].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[2].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[2].get_geometry()[1] > allWindows[3].get_geometry()[1]:
      bottomRight = allWindows[2]
      print(str(bottomRight.get_application().get_name()) + " is in the bottom right.")
      
  # Find out where Window 3 is.
  if allWindows[3].get_geometry()[0] < allWindows[0].get_geometry()[0] or allWindows[3].get_geometry()[0] < allWindows[1].get_geometry()[0] or allWindows[3].get_geometry()[0] < allWindows[2].get_geometry()[0]:
    # Window 3 is on the left.
    if allWindows[3].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[3].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[3].get_geometry()[1] < allWindows[2].get_geometry()[1]:
      topLeft = allWindows[3]
      print(str(topLeft.get_application().get_name()) + " is in the top left.")
    elif allWindows[3].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[3].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[3].get_geometry()[1] > allWindows[2].get_geometry()[1]:
      bottomLeft = allWindows[3]
      print(str(bottomLeft.get_application().get_name()) + " is in the bottom left.")
  elif allWindows[3].get_geometry()[0] > allWindows[0].get_geometry()[0] or allWindows[3].get_geometry()[0] > allWindows[1].get_geometry()[0] or allWindows[3].get_geometry()[0] > allWindows[2].get_geometry()[0]:
    # Window 3 is on the right.
    if allWindows[3].get_geometry()[1] < allWindows[0].get_geometry()[1] or allWindows[3].get_geometry()[1] < allWindows[1].get_geometry()[1] or allWindows[3].get_geometry()[1] < allWindows[2].get_geometry()[1]:
      topRight = allWindows[3]
      print(str(topRight.get_application().get_name()) + " is in the top right.")
    elif allWindows[3].get_geometry()[1] > allWindows[0].get_geometry()[1] or allWindows[3].get_geometry()[1] > allWindows[1].get_geometry()[1] or allWindows[3].get_geometry()[1] > allWindows[2].get_geometry()[1]:
      bottomRight = allWindows[3]
      print(str(bottomRight.get_application().get_name()) + " is in the bottom right.")

elif len(allWindows) != 4:
  print("This test requires four windows! Please reset the test.")
  exit()

if topLeft == None or bottomLeft == None or topRight == None or bottomRight == None:
  print("Unable to determine window positions! Please reset the test.")
  exit()

print("")

if getActiveWindow() == bottomRight:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " test is starting with bottom right window selected.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " bottom right window is not selected at beginning of test.")
  testsFailed += 1
  print("Bottom right application: " + str(bottomRight.get_application().get_name()))
  print("Selected application: " + str(getActiveWindowName()))


pyautogui.hotkey('winleft', 'left')
if getActiveWindow() == bottomLeft:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " bottom left window is selected after moving left from bottom right.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " bottom left window is not selected after moving left from bottom right.")
  testsFailed += 1
print("Active window: " + getActiveWindowName())
time.sleep(0.2)

pyautogui.hotkey('winleft', 'up')
if getActiveWindow() == topLeft:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " top left window is selected after moving up from bottom left.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " top left window is not selected after moving up from bottom left.")
  testsFailed += 1
print("Active window: " + getActiveWindowName())
time.sleep(0.2)

pyautogui.hotkey('winleft', 'right')
if getActiveWindow() == topRight:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " top right window is selected after moving right from top left.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " top right window is not selected after moving right from top left.")
  testsFailed += 1
print("Active window: " + getActiveWindowName())
time.sleep(0.2)

pyautogui.hotkey('winleft', 'down')
if getActiveWindow() == bottomRight:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " bottom right window is selected after moving down from top right.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " bottom right window is not selected after moving down from top right.")
  testsFailed += 1
print("Active window: " + getActiveWindowName())
time.sleep(0.2)

# TEST ITEM: Windows can be resized with the keyboard (Test resizing four windows above, below, right, and left to ensure shortcut consistency)

## Select the top-left window
pyautogui.hotkey('winleft', 'up')
pyautogui.hotkey('winleft', 'left')
if getActiveWindow() == topLeft:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " top left window is selected after moving up, left from bottom right.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " top left window is not selected after moving up, left from bottom right.")
  testsFailed += 1
# print("Active window: " + getActiveWindowName())
increaseWidth()
increaseHeight()
decreaseWidth()
decreaseHeight()

## Select the bottom-left window
pyautogui.hotkey('winleft', 'down')
if getActiveWindow() == bottomLeft:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " bottom left window is selected after moving down from top left.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " bottom left window is not selected after moving down from top left.")
  testsFailed += 1
# print("Active window: " + getActiveWindowName())
increaseWidth()
increaseHeight()
decreaseWidth()
decreaseHeight()

## Select the bottom-right window
pyautogui.hotkey('winleft', 'right')
if getActiveWindow() == bottomRight:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " bottom right window is selected after moving right from bottom left.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " bottom right window is not selected after moving right from bottom left.")
  testsFailed += 1
# print("Active window: " + getActiveWindowName())
increaseWidth()
increaseHeight()
decreaseWidth()
decreaseHeight()

## Select the top-right window
pyautogui.hotkey('winleft', 'up')
if getActiveWindow() == topRight:
  print(bcolors.PASS + "PASS:" + bcolors.ENDC + " top right window is selected after moving up from bottom right.")
  testsPassed += 1
else:
  print(bcolors.FAIL + "FAIL:" + bcolors.ENDC + " top right window is not selected after moving up from bottom right.")
  testsFailed += 1
# print("Active window: " + getActiveWindowName())
increaseWidth()
increaseHeight()
decreaseWidth()
decreaseHeight()

print("")
print(str(testsPassed) + " tests passed, " + str(testsFailed) + " tests failed.")
