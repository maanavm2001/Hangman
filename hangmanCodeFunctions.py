"""hangmanCodeFunctions

Author: Maanav Modi

This script is the hangmanCodeFunctions class. This class allows
users to call and create this hangman game object. This allows the
GUI class to transfer and recieve data and process the logic
for the actualy hangman game.

This class has a pre-existing word bank dictionary file (bagofworrds.txt)

This class can be imported as and contains the following public
functions:

    * letterAttempt - checks to see if game is won and
                      recieves user-input letter from GUI class
                      ,processes the letter detemining if it is in the words
                      ,returns True if the letter exists in the word
                      or False if it does not
                      , it will then add to the according set

    * getData - returns the current guessed string and string of incorrect
                guesses for GUI to call to output current guessed string and
                incorrect guesses for user
    
    * getGameWon - returns if the game has been won

    * getGameLost - returns if the game has been lost

    * setAttempts - sets game objects __attempts

    * getAttempts - returns game objects __attempts

    * getGuessWord - returns current game objects __guessWord (word to be guessed)
"""

import random
import sys
import time

class hangmanCodeFunctions:

    # Sets intial values, creates random word to guess
    # and creates a set of letters for the random wod generated
    #   attempts - user input for max attempts
    def __init__(self, attempts):
        attempts = int(attempts)
        self.__guessWord = ""
        guessWord = self.__guessWordGenerator() # creates the random guess word
        
        # creates the random guess word's set
        guessWordSet = self.__guessWordLetterSetBuilder(guessWord) 
        self.__guessWord = guessWord
        self.__attempts = attempts
        self.__correctGuesses = set()
        self.__incorrectGuesses = set()
        self.__guessWordSet = guessWordSet
    
    # This function opens the file, outs all the words into a list,
    # then returns a randomly selected word from the list
    def __guessWordGenerator(self):
        fileObj = open('bagofworrds.txt')
        listOfWords = []
        # goes line by line to append word to the list
        for line in fileObj:
            listOfWords.append(line.strip("\n"))
        return random.choice(listOfWords)
    
    # This function recieves the guess word and 
    # appends each indivdiual letter to a set 
    # which is then returned
    #   word - word to be used to create a set of letter
    def __guessWordLetterSetBuilder(self, word):
        characters = set()
        for element in range(0, len(word)):
            characters.add(word[element])
        return characters
    
    # This functions is the main processor for the user attempts
    # it recieves the user input letter guess
    # ,processes the letter detemining if it is in the words
    # ,returns True if the letter exists in the word
    # or False if it does not
    # , it will then add to the according set
    # and will also check tto see if the game is won by
    # checking to see if all charactes have been guessed
    #   letter - user input letter from GUI class
    def letterAttempt(self, letter):
        # checks if all letters have been gussed by comparing two sets
        if (self.__correctGuesses == self.__guessWordSet):
            return True
        # checks to see if user guess letter is in the set of letters 
        # of the guessWord
        elif(letter in self.__guessWordSet):
            self.__correctGuesses.add(letter)
            return True
        else:
            self.__incorrectGuesses.add(letter)
            self.__attempts -= 1
            return False
    
    # This functions returns the current guessed string and string of incorrect
    # guesses for GUI to call to output current guessed string and
    # incorrect guesses for user
    def getData(self):
        data = []
        userStringWord = ["_ "] * len(self.__guessWord)
        for letter in self.__correctGuesses:
            letterOccurence = (i for i,value in enumerate(self.__guessWord) 
                                 if value == letter)
            for index in letterOccurence:
                userStringWord[index] = letter + " "
        userString = ""
        for letter in userStringWord:
            userString += letter
        userIncorrectGuess = ""
        for elem in self.__incorrectGuesses:
            if(len(userIncorrectGuess) == 0):
                userIncorrectGuess += elem
            else:
                userIncorrectGuess += ", " + elem
        data.append(userString)
        data.append(userIncorrectGuess)
        return data    

    # returns if the game has been won
    def getGameWon(self):
        return self.__correctGuesses == self.__guessWordSet

    # returns if the game has been lost
    def getGameLost(self):
        return self.__attempts == 0
    
    # sets game objects __attempts
    def setAttempts(self, attempts):
        self.__attempts = attempts

    # returns game objects __attempts
    def getAttempts(self):
        return self.__attempts
    
    # returns current game objects __guessWord (word to be guessed)
    def getGuessWord(self):
        return self.__guessWord