import pandas as pd 
import PySimpleGUI as sg

# Custom imports
import ui
import process

# Initalize the GUI
gui = ui.UI()
window = gui.get_window()

# Initalize Processing Module
proc = process.Process()

while True:
    event, values = window.read()
    if event == 'Save':
        print('==> Save')

    if event == "Event":
        window.Maximize()
        print(window.size)

    if event == "Submit":
        print(values["-FILE-"])
        proc.set_data(values["-FILE-"])

    if event == sg.WIN_CLOSED or event == 'Exit':
        print("==> Exit")
        break
window.close()