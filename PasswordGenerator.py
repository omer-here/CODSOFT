# pip install tkinter
from tkinter import *
# pip install pyperclip
import pyperclip
import tkinter.messagebox
import random

root = Tk()
root.title("Password Generator")
root.geometry("600x200")
passwrd = StringVar()
passlen = IntVar()
passlen.set(8)       #default value


def generate(): # Function to generate the password
	characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(characters)
	passwrd.set(password) 
	tkinter.messagebox.showinfo(title="Info!", message="Password Generated!")

# function to copy the passcode
def copyclipboard():
	random_password = passwrd.get()
	pyperclip.copy(random_password)
	tkinter.messagebox.showinfo(title="Info!", message="Password Copied to CLipboard!")


# Labels
Label(root, text="Strong Password Generator", font="Courier 20 bold").pack()
Label(root, text="Type Your Password Lenght: ").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Click To Generate", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Tap to copy clipboard", command=copyclipboard).pack(pady=7)
root.mainloop()
