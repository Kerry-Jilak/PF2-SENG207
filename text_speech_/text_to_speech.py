#importing libraries
import pyttsx3
import PySimpleGUI as sg


#creating voice engine
engine=pyttsx3.init()
Voices=engine.getProperty('voices')
sg.theme('DarkBlue')
layout=[ 
[sg.Text('Select voice type: '),sg.Radio('Male voice', 'RADIO1', default=True, key='male_voice'),sg.Radio('Female', 'RADIO1', key='female_voice')],
[sg.Text('Enter text to speak:')],
[sg.InputText(key='INPUT'),sg.Button('Speak')]
]


#to create window
window=sg.Window('Text to speech app',layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['INPUT']
        if values['male_voice']:
            engine.setProperty('voice', Voices[0].id)
        elif values['female_voice']:
           engine.setProperty('voice', Voices[1].id) 
           
           
        engine.say(text)
        engine.runAndWait()

window.close()