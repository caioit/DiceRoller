import PySimpleGUI as sg
import random

sides = [1, 2, 3, 4, 5, 6]

#Generate a random number 
def randomization(sides):
    return(random.choice(sides))

result = randomization(sides)

#Elements in the Window
layout = [
    [sg.Text(result, key='RESULT')],
    [sg.Button('Roll'),sg.Button('Exit')]
]

#Create Window
window = sg.Window('Dice Roller', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Roll':
        result = randomization(sides)
        window['RESULT'].update(result)

    print(result)
    
window.close()

