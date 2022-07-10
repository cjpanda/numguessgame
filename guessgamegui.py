# imports
import tkinter as tk
import random 

# create a window
window = tk.Tk()
# set the dimensions of the window
window.geometry("600x400")
#background color of the window
window.config(bg='#084594')
window.resizable(width=False,height=False)
# window title
window.title('Number Guessing Game by cjpanda')
TARGET = random.randint(0, 100)
RETRIES = 0


def update_result(text):
    result.configure(text=text)

#Create New Game
def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET= random.randint(0, 100)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")

# Continue Ongoing game or End it 
def play_game():
    global RETRIES

    choice= int(number_form.get())
    if choice != TARGET:
        RETRIES += 1

        result = "Wrong Guess! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and \n{}".format(result)
        else:
            hint = "The required number lies between {} and\n 100".format(choice)
        result += "\n\nHINT :\n" + hint

    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"
     
    update_result(result)


# heading of the game
title = tk.Label(window,text="Guessing Game",font=("Helvetica",24),fg="#fffcbd",bg="#065569")
# Results and hints display
result = tk.Label(window, text="Click on Play to start a new game", font=("Helvetica", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
# Play Button
play_button = tk.Button(window, text="Play Game", font=("Helvetica", 14, "bold"), fg = "Black", bg="#ffd700", command=new_game)
# Guess Button 
guess_button = tk.Button(window,text="Guess",font=("Helvetica",13), state='disabled', fg="#ffd700",bg="Black", command=play_game)
# exit button for the window 
exit_button = tk.Button(window,text="Exit Game",font=("Helvetica",14),fg="white", bg="#b82741", command=exit)

# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Helvetica",11),textvariable=guessed_number)

# label Placements 
title.place(x=170, y=50)
result.place(x=180, y=210) 

# button positions 
exit_button.place(x=300,y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

# Entry field placement
number_form.place(x=180, y=150)

window.mainloop()