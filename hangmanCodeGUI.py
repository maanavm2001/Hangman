"""hangmanCodeFunctions

Author: Maanav Modi

This program is the hangmanCodeGUI progam. This file creates an inteactive
GUI frame that allows a user to play the game Hangman. This GUI recieves data
and creates a hangmanCodeFunctions object to run the logic for the game.

To run this program tkinter, ttk, and hangmanCodeFunctions is required.

This class can be ran and will have a GUI running the following methods:

    * hangmanGameStart - recieves the first user input
                          of guesses and creates a hangmanCodeFunctions
                          object with that attempts set. Once the attempts set
                          it calls a function, promptToGameTransition(), to 
                          transition to the start of the main game

    * promptToGameTransition - a brief transition to start the game. It then
                               clears all widgets off the screen and calls function,
                               mainGameGUI(), which creates a new screen to play the
                               main game.
    
    * mainGameGUI - the main GUI handler with all Labels, Combobox, and Button

    * letterEnter - button handler to process user letter input
                    which uses the hangmanCodeFunctions object to check if 
                    the letter is valid and to check if game is won/lost
                    If game is won or lost then it deletes all widgets with 
                    destoyWidgets() and prompts screen to ask user to restart
                    with function restartGame()

    * restartGame - end GUI that prompts user with Buttons to restart game
                    if yes-> restarts game from starts
                    if no-> closes program

    * startGame - function called by restartGame which restarts the program

    * destroyWidgets - destorys all Widgets in global list of widgets

    * pause - pauses the program for sec * 1000ms 
"""

import time
import os
from tkinter import *
from tkinter import ttk
from hangmanCodeFunctions import hangmanCodeFunctions

allWidgets = [] # global list of Widgets
hangmanGameObj = hangmanCodeFunctions(0) #initalizes hangmanGameObj

#Creates Tk object window
window = Tk()
window.title("Hangman Game")
window.geometry('800x800')
bg_bgColor = Canvas(window, width = 1920, height = 1080, bg = 'burlywood1')
bg_bgColor.place(relx = -0.1, rely = -0.1, anchor = "nw")
okVar = IntVar()
lbl_welcome = Label(window, text="Welcome To Hangman", 
                font=("Arial Bold", 50), bg = 'burlywood3')
lbl_welcome.place(relx = 0.5, rely = 0.0,
                       anchor = 'n')
lbl_attemptsPrompt = Label(window, text="How many possible attempts?[1-25] ", 
                font=("Arial", 25), bg = 'burlywood3')
lbl_attemptsPrompt.place(relx = 0.05, rely = 0.2,
                       anchor = 'w')
# combobox - user input for attempts                     
combobox_attemptsIn = ttk.Combobox(window, height = 4, width = 2, 
                                      values =[1,2,3,4,5,6,7,
                                               8,9,10,11,12,13,
                                               14,15,16,17,18,19
                                               ,20,21,22,23,24,25])
combobox_attemptsIn.place(relx=0.6, rely = 0.2, anchor = 'center')
# button - to enter user input and call hangmanStart()
btn_attempsSet = Button(window, text = 'Enter', command = lambda: hangmanGameStart(combobox_attemptsIn))
btn_attempsSet.place(relx = 0.66, rely = 0.2, anchor = 'center')

# This function recieves the first user input
# of guesses and creates a hangmanCodeFunctions
# object with that attempts set. Once the attempts set
# it calls a function, promptToGameTransition(), to 
# transition to the start of the main game
#   combobox_attempsIn - combobox widget containing user input for
#                        number of attempts
def hangmanGameStart(combobox_attemptsIn):
    # sets game objects attempts to user's input
    hangmanGameObj.setAttempts(int(combobox_attemptsIn.get()))
    promptToGameTransition()

# This function is a brief transition to start the game. It then
# clears all widgets off the screen and calls function,
# mainGameGUI(), which creates a new screen to play the
# main game.
def promptToGameTransition():
    pause(0.7)
    lbl_wordSelecting = Label(window, text="Selecting Word... ", 
                font=("Arial", 20), bg = 'burlywood3')
    lbl_wordSelecting.place(relx = 0.5, rely = 0.3,
                       anchor = 'center')
    lbl_gameToStart = Label(window, text="Word Selected... Game is about to begin!", 
                font=("Arial", 20), bg = 'burlywood3')
    pause(1)
    lbl_gameToStart.place(relx = 0.5, rely = 0.4,
                       anchor = 'center')
    pause(1.1)
    # destroys all widgets
    lbl_wordSelecting.destroy()
    lbl_attemptsPrompt.destroy()
    lbl_gameToStart.destroy()
    btn_attempsSet.destroy()
    combobox_attemptsIn.destroy()
    pause(0.7)
    mainGameGUI()

# This function is the main GUI handler with all Labels, Combobox, and Button
def mainGameGUI():
    lbl_letterPrompt = Label(window, text ="Select Letter: ",
                            font = ("Arial",25), bg= 'burlywood3')
    lbl_letterPrompt.place(relx = 0.1, rely = 0.3, anchor = 'w')
    # combobox - user input for letter to guess
    combobox_letterIn = ttk.Combobox(window, height = 4, width = 2, 
                                      values =['a','b','c','d','e','f'
                                      ,'g','h','i','j','k','l','m','n'
                                      ,'o','p','q','r','s','t','u','v'
                                      ,'w','x','y','z'])
    combobox_letterIn.place(relx=0.34, rely=0.3, anchor = 'w')
    lbl_attemptsLeft = Label(window, text = 'Attempts Left: ' + 
                        str(hangmanGameObj.getAttempts()), font = ('Arial', 30),
                            bg = 'burlywood3')
    lbl_incorrectGuesses = Label(window, text = "Incorrect Guesses: ", 
                        font = ('Arial', 25), bg = 'burlywood3')
    lbl_userWordGuess = Label(window, text = '_ ' * len(hangmanGameObj.getGuessWord()),
                              font = ('Arial', 50), bg = 'burlywood1')
    # btn - to enter user input letter and call letterEnter
    btn_letterSet = Button(window, text = 'Enter', 
                           command = lambda: letterEnter(combobox_letterIn, 
                           lbl_attemptsLeft, lbl_incorrectGuesses,
                           lbl_userWordGuess))
    btn_letterSet.place(relx = 0.4, rely = 0.3, anchor = 'w')
    lbl_incorrectGuesses.place(relx = 0.1, rely = 0.42, anchor = 'w')  
    lbl_userWordGuess.place(relx = 0.5, rely = 0.7, anchor = 's')
    lbl_attemptsLeft.place(relx = 0.8,rely=0.3, anchor = 'e')   
    # adds all widets to allWidgets list
    allWidgets.append(lbl_letterPrompt)   
    allWidgets.append(combobox_letterIn) 
    allWidgets.append(lbl_incorrectGuesses)
    allWidgets.append(lbl_userWordGuess) 
    allWidgets.append(btn_letterSet) 
    allWidgets.append(lbl_attemptsLeft) 

# This function is the button handler to process user letter input
# which uses the hangmanCodeFunctions object to check if 
# the letter is valid and to check if game is won/lost
# If game is won or lost then it deletes all widgets with 
# destoyWidgets() and prompts screen to ask user to restart
# with function restartGame()
#   combobox_letterIn - user input for letter to guess
#   lbl_attemptsLeft - Label that tells user attempts left
#   lbl_incorrectGuesses - Label that tells user their current incorrect guesses
#   lbl_userWordGuess - Label that tells user current correct letters in the guessWord
def letterEnter(combobox_letterIn, lbl_attemptsLeft,lbl_incorrectGuesses, lbl_userWordGuess):
    # sends letter to game object hangmanGameObj
    letterIn = hangmanGameObj.letterAttempt(combobox_letterIn.get()) 
    # updates attempts in attemptsLeft Label
    lbl_attemptsLeft.config(text = 'Attempts Left: ' + 
                        str(hangmanGameObj.getAttempts())) 
    # gets current data; correct sting from corrrect guesses, and incorrect guesses
    toPrintList = hangmanGameObj.getData()
    # updates the users incorrect guesses and the users current correct letters in the guessWord
    lbl_incorrectGuesses.config(text = "Incorrect Guesses: " + toPrintList[1])
    lbl_userWordGuess.config(text = toPrintList[0])
    gameWon = hangmanGameObj.getGameWon() 
    gameLost = hangmanGameObj.getGameLost()
    # checks to see if game has been won or lose
    if(gameWon):
        lbl_gameWon = Label(window,text = "GAME WON!",
                          font = ("Arial", 60), bg = "burlywood3")
        allWidgets.append(lbl_gameWon)
        lbl_gameWon.place(relx = 0.5,rely = 0.9, anchor = 's' )
        pause(1.2)
        destroyWidgets()
        pause(0.3)
        restartGame()
    elif(gameLost):
        lbl_gameLoss = Label(window,text = "GAME LOST",
                          font = ("Arial", 60), bg = "burlywood3")
        allWidgets.append(lbl_gameLoss)
        lbl_gameLoss.place(relx = 0.5,rely = 0.9, anchor = 's' )
        pause(1.2)
        destroyWidgets()
        pause(0.3)
        restartGame()

# This function is the end GUI that prompts user with Buttons to restart game
# if yes-> restarts game from starts
# if no-> closes program
def restartGame():
    lbl_restartGame = Label(window, text = "Restart Game?", 
                            font = ("Arial", 25), bg = 'burlywood3')
    allWidgets.append(lbl_restartGame)
    lbl_restartGame.place(relx = 0.5, rely = 0.3, anchor = 'center')
    btn_yes = Button(window, text = "Yes", font = ("Arial", 25)
                    ,command= lambda: startGame())
    btn_yes.place(relx = 0.3, rely = 0.35, anchor = 'w')
    btn_no = Button(window, text = "No", font = ("Arial", 25)
                    ,command= lambda: window.destroy())
    btn_no.place(relx = 0.62, rely = 0.35, anchor = 'w')

# function called by restartGame which restarts the program
def startGame():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# destorys all Widgets in global list of widgets
def destroyWidgets():
    for elem in allWidgets:
        elem.destroy()

# pauses the program for sec * 1000ms 
def pause(sec):
    var = IntVar()
    window.after(int(1000 * sec) , var.set, 1)
    window.wait_variable(var)

window.mainloop()