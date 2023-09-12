import PySimpleGUI as sg
import uuid
import pyperclip

uuidString = str(uuid.uuid4())

sg.theme('DarkAmber')

layout = [
    [sg.InputText({uuidString})],
    [sg.Button("Sair"), sg.Button("Gerar"), sg.Button("Copiar")]
]

window = sg.Window("GUID Generate by R", layout, margins=(270, 170))

while True:
    event, values = window.read()

    if event == "Sair":
        break

    elif event == "Gerar":
        uuidString

    elif event == "Copiar":
        pyperclip.copy(f'{str(uuidString)}')



