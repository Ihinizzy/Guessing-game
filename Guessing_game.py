import random as rd
from typing import Counter
import csv
from csv import writer
import time


# SET PLAY LIMIT TO 10 TRIES THEN DELAY GAME FOR 10 SECONDS 


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

    tries = 0  # add a counter and make it empty at first

    rand, name = collect_data()

    while True:

        guess_number = input("Guess number ")
        guess_number = int(guess_number) #TYPE CASTING 
        tries += 1 # increment at every try

        if guess_number == rand:
            
            print("YOU WIN")
            break

        elif guess_number < rand:

            print("HINT: YOUR NUMBER IS LESS")

        elif guess_number > rand:
            print("HINT: YOUR NUMBER IS MORE")

        else:
            pass
    write_to_file(name, tries)
    print("you tried:", tries, "times")





with open("database.csv", "a") as our_log_file:

    name = "israel"
    tries = 6
    our_log_file.write(f"{name},{tries}")


def write_to_file(name, tries):
    
    with open("database.csv", "a") as our_log_file:  #FILE OPE

        our_log_file.write(f"{name},{tries}\n") #\n means new 

    print("Logged session.!!")

write_to_file("Israel", 29)

play()  
