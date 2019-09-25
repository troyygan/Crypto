import pyperclip
 
pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.paste()

if not pyperclip.is_available():
    print("Copy functionality unavailable!")

