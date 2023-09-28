import PySimpleGUI as sg
import uuid
import pyperclip

uuidString = ''
textMultiline = []
messageString = ''

sg.theme('DarkTeal 7')

layout = [
    [sg.Multiline(f'{textMultiline}\n', key='textInput', expand_x=True, expand_y=True), sg.Text(f'{messageString}', key='textCopied')],
    [sg.Button("Gerar"), sg.Button("Copiar"), sg.Button("Sair")]
]

window = sg.Window("GUID Generate by R", layout, margins=(270, 170))

while True:
    event, values = window.read()

    if event in ("Sair", sg.WINDOW_CLOSED):
        break

    elif event == "Gerar":
        uuidString = str(uuid.uuid4())
        textMultiline.append(f'{uuidString}\n')
        window['textInput'].update(textMultiline)

    elif event == "Copiar":
        pyperclip.copy(f'{str(uuidString)}')
        messageString = 'Copied!'
        window['textCopied'].update(messageString)

window.close()