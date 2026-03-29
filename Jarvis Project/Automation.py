from os import startfile
from tkinter.messagebox import Message
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def WhatsappMsg(name, message):
    sleep(10)
    click(x=195, y=115)
    sleep(1)
    write(name)
WhatsappMsg('karan',Message)

def WhatsappMsg(name, message):
    
    sleep(10)
    click(x=195, y=115)
    sleep(1)
    write(name)
    sleep(0.5)
    click(x=188, y=249)
    sleep(0.5)
    click(x=571, y=690)
    sleep(0.5)
    write(message)
    press('enter')

    
