import PySimpleGUI as sg
import uuid
import pyperclip

uuidString = ''
messageString = ''

sg.theme('DarkAmber')

layout = [
    [sg.InputText(f'{uuidString}', key='textInput'), sg.Text(f'{messageString}', key='textCopied')],
    [sg.Button("Gerar"), sg.Button("Copiar"), sg.Button("Sair")]
]

window = sg.Window("GUID Generate by R", layout, margins=(270, 170))

while True:
    event, values = window.read()

    if event == "Sair" or event == sg.WINDOW_CLOSED:
        break

    elif event == "Gerar":
        uuidString = str(uuid.uuid4())
        window['textInput'].update(uuidString)

    elif event == "Copiar":
        pyperclip.copy(f'{str(uuidString)}')
        messageString = 'Copied!'
        window['textCopied'].update(messageString)

window.close()