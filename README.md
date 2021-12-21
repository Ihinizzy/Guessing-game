# Guessing-game
import random as rd
from typing import Count
import csv
from csv import writer
import time

def collect_data():

    figure = input("input figure \n: ")
    name = input("input name \n> ")

    figure = figure.split(" ")

    fig = map(lambda a: int(a), figure)
    fid = list(fig)

    rand = rd.randrange(fid[0], fid[1])
    print(rand)
    return rand, name

def play():

    limit = 1
    tries = 0  # add a counter and make it empty at first

    rand, name = collect_data()

    while limit <= 10:

        guess_number = input("Guess number ")
        guess_number = int(guess_number) #TYPE CASTING 
        tries += 1 # increment at every try
        limit += 1

        if guess_number == rand:
            
            print("YOU WIN")
            break

        elif guess_number < rand:

            print("HINT: YOUR NUMBER IS LESS")

        elif guess_number > rand:
            print("HINT: YOUR NUMBER IS MORE")

        if limit   == 10:
            print("you missed it ", tries, "times")
            print("we are now delaying you.")
            limit = 1
            time.sleep(10)


    write_to_file(name, tries)
    print("you tried:", tries, "times")


def write_to_file(name, tries):
    
    with open("database.csv", "a") as our_log_file:  #FILE OPEN CONTEXT MANAGER

        our_log_file.write(f"{name},{tries}\n") #\n means new line 

    print("Logged session.!!")


play()