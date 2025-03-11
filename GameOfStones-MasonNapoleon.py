##### Game of Stones - Mason Napoleon

### Initial imports, lists, and variable setup

import random
import time
num_stones = random.randint(17, 19)
valid_player_turn_request_answers = {"Yes", "Yeah", "yes", "yeah", "No", "no"}
yes_answers = {"Yes", "Yeah", "yes", "yeah"}
no_answers = {"No", "no"}
valid_stone_removal_count = {1, 2, 3}

### Asking player if they want to go first or second

def setup():
    ### Welcome Message
    print("Welcome to the Game of Stones!")
    time.sleep(2)
    print("Thanks for playing this version instead of Bryan Christopher Crane's.")
    time.sleep(3.5)
    print("His version sucks.")
    time.sleep(1.75)
    print("Probably.")
    time.sleep(1.3)
    ### Asking Player if they want to go first or second
    global current_turn
    global valid_player_turn_request_answers
    player_turn_request_validity = 0
    ### Only accepting answer if the player responds validly
    while player_turn_request_validity != 1:
        player_turn_request = input("Would you like to go first?  ")
        if player_turn_request in valid_player_turn_request_answers:
            player_turn_request_validity = 1
        else:
            print(end = "Please answer the question:  ")
    ### Converting Player's answer into easy turn code
    if player_turn_request in yes_answers:
        current_turn = 0
    elif player_turn_request in no_answers:
        current_turn = 1

def humans_turn():
    ### Asking Player how many stones they would like to remove
    global num_stones
    global valid_stone_removal_count
    player_stone_removal_request_validity = 0
    if num_stones != 1:
        print("There are now", num_stones, "stones remaining.")
    else:
        print("There is now", num_stones, "stone remaining.")
        time.sleep(.6)
    while player_stone_removal_request_validity != 1:
        ### Only accepting answer if the player chooses 1, 2, or 3 stones removed
        try:
            player_stone_removal_count = int(input("How many stones would you like to take?  "))
            if player_stone_removal_count in valid_stone_removal_count and player_stone_removal_count <= num_stones:
                player_stone_removal_request_validity = 1
                num_stones -= player_stone_removal_count
            elif player_stone_removal_count in valid_stone_removal_count and player_stone_removal_count > num_stones:
                if num_stones != 1:
                    print("There are only", num_stones, "stones remaining")
                else:
                    print("There is only", num_stones, "stone remaining")
            else:
                print("Please enter a number 1 - 3:  ")
        except ValueError:
            print("Please enter a number:  ")
    time.sleep(.6)
    ### Checking if Player won
    if num_stones <= 0:
        print()
        print()
        print("You won against the computer! Nice job!")

def computers_turn():
    global num_stones
    computers_stones_removed = 0
    if num_stones != 1:
        print("There are now", num_stones, "stones remaining.")
    else:
        print("There is now", num_stones, "stone remaining.")
    time.sleep(.6)
    ### Computer removes the stones in a way that will be best for them to win
    if num_stones %4 != 0:
        computers_stones_removed += num_stones %4
    else:
        computers_stones_removed += random.randint(1, 3)
    num_stones -= computers_stones_removed
    if computers_stones_removed != 1:
        print("The computer removed", computers_stones_removed, "stones.")
    else:
        print("The computer removed", computers_stones_removed, "stone.")
    time.sleep(.6)
    ### Checking if Computer won
    if num_stones <= 0:
        print()
        print()
        print("\nThe computer took the last stone and now there are 0 stones remaining.", "The computer beat you! NOOOOOOOOOO :(")


#######   Playing Game   #######


setup()
if current_turn == 0:
    while num_stones > 0:
        humans_turn()
        if num_stones > 0:
            computers_turn()
elif current_turn == 1:
    while num_stones > 0:
        computers_turn()
        if num_stones > 0:
            humans_turn()