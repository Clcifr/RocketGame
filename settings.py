import pygame

#screen:
info = pygame.display.Info()
WIDTH, HEIGHT  = info.current_w, info.current_h
FPS = 60
TITLE = "Atlas Rising"
#colours:
white = (255, 255, 255)
Black = (0, 0, 0)

#game rules:
gameLives = 3
correctScore = 10
incorrectScore = -5

#fonts
FONT_FILE = "assets/fonts/Oxanium_Medium"
FONT_SIZES = {
    "Title" : 45,
    "Subtitle" : 20, 
    "General" : 14,
}

#rocket

#animation timers

#gas laws questions
questionDict = [
    {"question" : "The rocket's combustion chamber is sealed by a piston with a cross-sectional area of 0.02 m² during ignition hot gases exert a force of 4000 N on the piston. If the pressure exceeds safe limits the chamber will break. Calculate the pressure inside the chamber." ,
    "answer" : "200,000" ,
    "unit" : "Pa"},
    {"question" : "The rocket uses liquid fuel stored in a vertical tank 5 m deep. The fuel has a density of 800 kg/m³. To reinforce the base of the tank, you must know the pressure at the bottom due to the fuel column. Calculate the pressure at the base of the tank. (Use g as 10 m/s².)" ,
    "answer" : "40",
    "unit" : "kPa"},
    {"question": "Before ignition, the gas inside the rocket chamber is compressed.Initial pressure: 100 kPa and Initial volume: 0.5 m³ The volume is reduced to 0.25 m³ while temperature remains constant. If pressure rises too high, the system will fail. Calculate the new pressure after compression" , 
    "answer" : "200" , 
    "unit" : "kPa",
    }
]