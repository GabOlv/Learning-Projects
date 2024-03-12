'''
    Project only to learn how to to make a simple interface and fetch some items from YouTube, 
    all the test was made using No Copyright Sounds
''' 

import PySimpleGUI as sg # Version 4.60.5
from pytube import YouTube
import os

# Defines the layout of and centralize them on the center
def create_layout():
    layout = [
        [sg.Column([[sg.Text('Youtube Video Downloader')]], justification='center')],
        [sg.Column([[sg.InputText(key='-INPUT-')]], justification='center')],
        [sg.Column([[sg.Button('Clear'), sg.Button('OK'), sg.Button('Select Folder')]], justification='center')],
        [sg.Column([[sg.Text('Path of the files')]], justification='center')],
        [sg.Column([[sg.Input(key='-OUTPUT_PATH-', readonly=True, disabled_readonly_background_color=sg.theme_background_color())]], justification='center')],
    ]
    return layout

# handles the logic using PyTube to fetch, verify, extract the audio and download the file
def download_file_function(values, folder_path):
    link_path = YouTube(values['-INPUT-'])
    if link_path == '':
        sg.popup("Need a Link", title='Error', font=('Arial',12))
        return
    else:
        try:
            # extract only the audio
            video = link_path.streams.filter(only_audio=True).first() 
            # download the file 
            out_file = video.download(output_path=folder_path) 
            # save the file
            base, ext = os.path.splitext(out_file)
            # rename the file with the extension
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            sg.popup(link_path.title + ' has been successfully downloaded.', title='Done', font=('Arial',12))
        except Exception:
            sg.popup('Error, the link dont work', title='Error', font=('Arial',12))
            
# Clear the link Input
def window_clear(window):
    window['-INPUT-'].update('')

# Path of the savefiles (TODO: Verify valid)
def select_folder(window): 
    folder_path = sg.popup_get_folder('Select Folder')
    if folder_path:
        #sg.popup(f'Selected Folder: {folder_path}')
        window['-OUTPUT_PATH-'].update(folder_path)
    return folder_path

# main_loop
def main_loop():
    #folder_path = ''
    # Window Creation and Style
    sg.theme('DarkAmber')
    window = sg.Window('Youtube Video Downloader', create_layout(), size=(400, 200))
    
    # Main Loop of the function
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # Close the aplication
            break
        
        # Clear the input text
        if event == 'Clear': 
            window_clear(window)
            
        # Process the elements
        if event == 'OK': 
            try:
                if (folder_path != ''):
                    download_file_function(values, folder_path)
                else:
                    sg.popup("Error, Verify Folder path", title='Error', font=('Arial',12))
            except Exception:
                sg.popup("Error, Verify Link", title='Error', font=('Arial',12))
        
        # Select the output folder, must exist
        if event == 'Select Folder': # Select the folder wich the audios will be saved
            folder_path = select_folder(window)
            if folder_path == None:
                folder_path = ''
                window['-OUTPUT_PATH-'].update('')
        
    window.close() # Close the window outside the main loop

# Starter of the algorithm
if __name__ == '__main__':
    main_loop()
