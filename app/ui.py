import PySimpleGUI as sg

class UI:
    def __init__(self):
        '''
        Define the initial layout of the window. 
        '''
        self.theme = 'Dark Grey 9'
        self.main_padding = (25, 25)
        self.main_background_color = '#2b2b2b'

        sg.theme(self.theme)

        self.top_banner = [[sg.Text('Dashboard', font='Any 20')]]

        self.main_block = [[sg.Text('Input File:', font='Any 20')], [sg.Text("")],
         [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-FILE-")],
         [sg.Button('Submit')]]

        self.bottom_banner = [[sg.Button('Exit', pad=(10,10), auto_size_button=True)]]

        self.layout = [[sg.Column(self.top_banner, size=(2400, 180), justification='center', pad=self.main_padding)],
                [sg.Column(self.main_block, size=(2400, 720), justification='center',  pad=self.main_padding)],
                [sg.Column(self.bottom_banner, size=(2400, 60), justification='center', pad=self.main_padding)]]

        self.window = sg.Window('Dashboard', self.layout, margins=(10,10), resizable=True, background_color=self.main_background_color, grab_anywhere=True, finalize=True)

    def get_window(self):
        return self.window