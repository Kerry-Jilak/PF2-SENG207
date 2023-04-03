import PySimpleGUI as sg
import qrcode
import os




def generate_qr_code(URL):
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=3,
            box_size=14,
            border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    doc_name = "qr_code"+ ".jpg"
    path = os.path.join(os.getcwd() ,doc_name)
    img.save(path)
    return path


sg.theme('DarkTanBlue')
layout = [
    [sg.Input(key='-URL-')],
    [sg.Button('Generate your QR Code', key='-Generate_QR _Code-')],
    [sg.Image(key='-PICTURE-', size=(250, 300))]
]

window = sg.Window('QR Code Generator', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-Generate_QR _Code-' :
        uRL= values['-URL-']
        qr_code_picture_path = generate_qr_code(uRL)
        window['-PICTURE-'].update(filename=qr_code_picture_path)

window.close()
