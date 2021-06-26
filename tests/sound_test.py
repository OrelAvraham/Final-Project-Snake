import pygame
from tkinter import *


def play():
    """
    Play main (background) music
    :return: None
    """
    pygame.mixer.music.load('../images/bg.mp3')
    pygame.mixer.music.play()


def pause():
    """
    Pause the main (background) music
    :return: None
    """
    pygame.mixer.music.pause()


def unpause():
    """
    Unpause the main (background) music
    :return: None
    """
    pygame.mixer.music.unpause()


def sound():
    """
    Make one-time sound effect
    :return:
    """
    pygame.mixer.Sound.play(sound_effect)


pygame.init()  # Initializing pygame
sound_effect = pygame.mixer.Sound('../images/food.mp3')  # creating the sound for the sound effect

# Starting root for Tkinter module
root = Tk()
root.geometry('180x200')

# Creating the frame for the sound looper
myframe = Frame(root)
myframe.pack()
mylabel = Label(myframe, text="Pygame Mixer")
mylabel.pack()

# Defining the buttons
button1 = Button(myframe, text="Play", command=play, width=15)
button1.pack(pady=5)
button2 = Button(myframe, text="Sound", command=sound, width=15)
button2.pack(pady=5)
button3 = Button(myframe, text="Unpause", command=unpause, width=15)
button3.pack(pady=5)
button4 = Button(myframe, text="Pause", command=pause, width=15)
button4.pack(pady=5)

# Running the main loop of the root (of Tkinter)
root.mainloop()


