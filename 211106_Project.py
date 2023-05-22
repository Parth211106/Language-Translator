"""
Parth Sharma 211106 CS31
Arun Thakur 211110 CS31
"""

from tkinter import *
from translate import Translator

# Translator function

def translate():
    translator= Translator(from_lang=language_for_translation.get(), to_lang=translated_language.get())
    translation = translator.translate(var.get())
    var1.set(translation)

# Tkinter root Window with Title

root = Tk()
root.title("LANGUAGE TRANSLATOR")

# Creating a Frame and Grid to hold the Content

main_frame = Frame(root)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
main_frame.columnconfigure(0, weight = 1)
main_frame.rowconfigure(0, weight = 1)
main_frame.pack(pady = 200, padx = 200)
root.config(bg="light pink")

# Variable names for dropdown list

language_for_translation = StringVar(root)
translated_language = StringVar(root)

# Choices to show in dropdown menu

choices = { 'English','Hindi','Gujarati','Spanish','German'}

# Default selection for dropdownlists

language_for_translation.set('English')
translated_language.set('Hindi')

# Creating dropdown and arranging in the grid

language_for_translation_menu = OptionMenu(main_frame, language_for_translation, *choices)
Label(main_frame, text="Select language").grid(row = 0, column = 1)
language_for_translation_menu.grid(row = 1, column =1)

translated_language_menu = OptionMenu(main_frame, translated_language, *choices)
Label(main_frame, text="Select Language").grid(row = 0, column = 2)
translated_language_menu.grid(row = 1, column =2)

# textBox to take user input

Label(main_frame, text ="Enter text").grid(row=2, column=0)
var = StringVar()
textbox = Entry(main_frame, textvariable=var).grid(row=2, column=1)

# textbox to show output and label can also be used

Label(main_frame, text ="Translation").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(main_frame, textvariable=var1).grid(row=2, column=3)

# Creating a button to call Translator function

b=Button(main_frame, text='Translate', command=translate).grid(row=3, column=1, columnspan=3)

root.mainloop()
