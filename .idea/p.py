import sys
import time

def printlyrics():
    lineas = [
        "Drinks in the room, it's just us two",
        "Drinks in the room, it's just us two, girl",
        "Down the whole thing if you want to",
        "Down the whole thing, show me you a big girl",
        "I'm rockin' two chains, bumpin' 2 Chainz",
        "In a Rolls Royce, ain't a damn thing",
        "Ain't a fluke, baby, it's the truth, baby",
        "Cause the sex game got me in a loop, baby"
    ]

    delays = [1.0, 0.5, 1.0, 0.3, 0.6, 0.4, 0.5, 0.7]

    for i, (linea, line_delay) in enumerate(zip(lineas, delays)):
        # Cambiar color a púrpura (ANSI escape)
        sys.stdout.write("\033[95m")
        sys.stdout.flush()
        
        for char in linea:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Delay por cada letra
        
        # Resetear color y hacer nueva línea
        sys.stdout.write("\033[0m\n")
        sys.stdout.flush()

        # Delay entre líneas
        time.sleep(line_delay)

# Ejecutar la función
printlyrics()
         