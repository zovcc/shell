#!/usr/bin/env python3

import pyautogui
import time
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from gi.repository import Gtk

print("")

def getAllWindows():
  time.sleep(1)
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while Gtk.events_pending():
    Gtk.main_iteration()
  time.sleep(0.5)
  return screen.get_windows()

def getActiveWindow():
  time.sleep(1)
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while Gtk.events_pending():
    Gtk.main_iteration()
  time.sleep(0.5)
  return screen.get_active_window()

def getActiveWindowName():
  time.sleep(1)
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
  print("PASS: test is starting with bottom right window selected.")
else:
  print("FAIL: bottom right window is not selected at beginning of test.")
  print("Bottom right application: " + str(bottomRight.get_application().get_name()))
  print("Selected application: " + str(getActiveWindowName()))


pyautogui.hotkey('winleft', 'left')
if getActiveWindow() == bottomLeft:
  print("PASS: bottom left window is selected after moving left from bottom right.")
else:
  print("FAIL: bottom left window is not selected after moving left from bottom right.")
print("Active window: " + getActiveWindowName())

pyautogui.hotkey('winleft', 'up')
if getActiveWindow() == topLeft:
  print("PASS: top left window is selected after moving up from bottom left.")
else:
  print("FAIL: top left window is not selected after moving up from bottom left.")
print("Active window: " + getActiveWindowName())

pyautogui.hotkey('winleft', 'right')
if getActiveWindow() == topRight:
  print("PASS: top right window is selected after moving right from top left.")
else:
  print("FAIL: top right window is not selected after moving right from top left.")
print("Active window: " + getActiveWindowName())

pyautogui.hotkey('winleft', 'down')
if getActiveWindow() == bottomRight:
  print("PASS: bottom right window is selected after moving down from top right.")
else:
  print("FAIL: bottom right window is not selected after moving down from top right.")
print("Active window: " + getActiveWindowName())

