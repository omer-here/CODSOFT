# pip install tkinter
#https://www.learnpython.org/
from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("Rock Paper & Scissors")
root.geometry("600x250")

options = ["rock", "paper", "scissors"]

def Play():
    computersTurn = random.choice(options)
    playersTurn = clicked.get()
    
    #tkinter.messagebox.showinfo(title="Info!", message="Computers Turn: "+ computersTurn)
    
    #Game Logic
    if computersTurn == playersTurn:
        result.set(" It's a tie!")
    elif playersTurn == "rock":
        if computersTurn == "scissors":
            result.set("Rock Samshes Scissors, You won")
            Player.set(Player.get()+1)
        elif computersTurn == "paper":
            result.set("Paper covers the rock, You Lost")
            Computer.set(Computer.get()+1)
    elif playersTurn == "paper":
        if computersTurn == "rock":
            result.set("Paper covers the rock, You won")
            Player.set(Player.get()+1)
        elif computersTurn == "scissors":
            result.set("scissors cuts the paper, You Lost")
            Computer.set(Computer.get()+1)
    elif playersTurn == "scissors":
        if computersTurn == "paper":
            result.set("scissors cuts the paper, You won")
            Player.set(Player.get()+1)
        elif computersTurn == "rock":
            result.set("Rock Smashes scissors, You Lost")
            Computer.set(Computer.get()+1)
    

#GUI
Label(root, text="Tap Play to Start!", font="Courier 20 bold").pack()


# datatype of menu text 
clicked = StringVar()
result = StringVar() 
Computer  = IntVar()
Player = IntVar()

# initial menu text 
clicked.set( "Choose Your Option" ) 
result.set("Select & hit Play")
Computer.set(0)
Player.set(0)

  
# Create Dropdown menu 
drop = OptionMenu( root, clicked , *options ) 
drop.pack()

#Play Button
Button(root, width=10, text="Play", command=Play).pack(pady=7)

#Displaying the Result
Label(root, textvariable=result).pack(pady=3)

#Scoring Labels
Label(root, text="Computer's Score").pack()
Label(root, textvariable=Computer, font="Courier 15 bold").pack(pady=3)

Label(root, text="Player's Score").pack()
Label(root, textvariable=Player, font="Courier 15 bold").pack(pady=3)




root.mainloop()