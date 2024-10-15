from downloadMP3 import download_audio
from tkinter import messagebox

def start_down():
    url = music
    path = path_set
    if download_audio(url, path):
        messagebox.showinfo("Вы установили музику")
    else:
        messagebox.showerror("Не получилось")

        

music = input("Введите силку: ")
path_set = "./music"

start_down()