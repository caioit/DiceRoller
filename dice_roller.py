import PySimpleGUI as sg
import random

class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.side = []
        
        for i in range(number_of_sides):
            self.side.append(i + 1)
    
    def print_sides(self):
        print(self.side)

number_of_sides = 6
dice = Dice(number_of_sides)

#Generate a random number 
def randomization(sides):
    return(random.choice(sides))

result = randomization(dice.side)

#Elements in the Window
layout = [
    [sg.Text(result, key='RESULT', size=(30,2))],
    [sg.Button('Roll'),sg.Button('Exit')]
]

#Create Window
window = sg.Window('Dice Roller', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Roll':
        result = randomization(dice.side)
        window['RESULT'].update(result)

    print(result)
    
window.close()

