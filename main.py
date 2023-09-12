import PySimpleGUI as sg
import uuid

uuidString = str(uuid.uuid4())

layout = [[sg.InputText({uuidString})], [sg.Button("Sair"), [sg.Button("Gerar")]]]

window = sg.Window("GUID Generate by R", layout, margins=(270, 170))

while True:
    event, values = window.read()

    if event == "Sair":
        break

    elif event == "Gerar":
        uuidString = uuid.uuid4()



