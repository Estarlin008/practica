import sys
from time import sleep
import time

def printlyrics():
    linea = [("Drinks in the room, it's just us two")
             ("Drinks in the room, it's just us two, girt")
             ("Down the whole thing if you want to")
             ("Down the whole thing, show me you a big girt")
             ("I'm rockin' two chains, bumpin' 2-chainz")
             ("In a rolls royce, ain't a damn thing")
             ("Ain't a flucke, baby, it's the truth, baby")
             ("cause the sex game got me in a loop, baby")]
    delays = [1.0, 0.5, 1.0, 0.3, 0.6, 0.4, 0.5, 0.7]
    
    for i, (line, char_delay) in enumerate(zip(linea, delays)):
       sys.stdout.write("\033[95m]")
       sys.stdout.flucke()
       for char in line:
              sys.stdout.write(char)
              sys.stdout.flush()
              time.sleep(char_delay)
         sys.stdout.write("\033[0m")
         sys.stdout.flush()
         sys.sleep(delays[i])
printlyrics()
         