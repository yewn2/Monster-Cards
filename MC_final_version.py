"""
Monster Cards final version
This is the version that will be marked
"""


# imports
import easygui


# function to welcome user and show instructions
def welcome_instructions(program_name, instruction_list):
    # display welcome screen
    easygui.msgbox(f"Welcome to {program_name}!", "Welcome")

    # display instructions
    instructions = [f"Instructions for use of {program_name}\n"]
    for inst in instruction_list:
        instructions.append(f"\n* {inst} *")
    easygui.msgbox("".join(instructions), "Instructions")


# function to display action screen
def action_screen(cards):
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "MONSTER CARD DATABASE EDITOR",
                               ["Add card", "Delete card",
                                "Find card", "Edit card", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # check the choice and call the appropriate function
        if choice == "Add card":
            add_card(cards)
        elif choice == "Delete card":
            delete_card(cards)
        elif choice == "Find card":
            find_card(cards)
        elif choice == "Edit card":
            edit_card(cards)
        elif choice == "Output all":
            output_all(cards)

        # display action screen with choices again
        choice = easygui.buttonbox("What would you like to do?",
                                   "MONSTER CARD DATABASE EDITOR",
                                   ["Add card", "Delete card",
                                    "Find card", "Edit card", "Output all", "Exit"])

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Monster Cards",
                   "Goodbye!")


# function to add a card
def add_card(database):
    # ask user for card name
    new_monster = easygui.enterbox("Enter a name for your new monster card:",
                                   "New Monster")

    confirm_monster = ""
    # making sure the new name is not an empty string or the NoneType value
    if new_monster is not None:
        if new_monster.replace(" ", "") != "":
            # name confirmation
            confirm_monster = easygui.buttonbox(f"The name you want to have for your new "
                                                f"card is {new_monster}.",
                                                "Monster Name Confirmation",
                                                ["Yes", "No"])

            # check if card already exists in the dictionary
            if new_monster.lower() in (monster_name.lower() for monster_name in database):
                confirm_monster = "Present"
        else:
            easygui.msgbox("You have not entered a name for your new card.", "No Name")
    else:
        return

    while confirm_monster != "Yes":
        # if the card name is already existing inform the user
        if confirm_monster == "Present":
            easygui.msgbox(f"The card name {new_monster} is already present in the card "
                           f"database.",
                           "Card already exists")
        # ask user for card name again
        new_monster = easygui.enterbox("Enter a name for your new monster card:",
                                       "New Monster")
        confirm_monster = ""
        if new_monster is not None:
            if new_monster.replace(" ", "") != "":
                # name confirmation again
                confirm_monster = easygui.buttonbox(f"The name you want to have for your new "
                                                    f"card is {new_monster}.",
                                                    "Monster Name Confirmation",
                                                    ["Yes", "No"])

                # check if card already exists in the dictionary
                if new_monster.lower() in (monster_name.lower() for monster_name in database):
                    confirm_monster = "Present"
            else:
                easygui.msgbox("You have not entered a name for your new card.", "No Name")
        else:
            return

    # add card name to card database; set stat categories by default  to 0
    database[new_monster] = {}
    database[new_monster]["Strength"] = "0"
    database[new_monster]["Speed"] = "0"
    database[new_monster]["Stealth"] = "0"
    database[new_monster]["Cunning"] = "0"

    # entering stats for new card
    monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                      f"current stats are:\n"
                                      f"\tStrength: "
                                      f"{database[new_monster]['Strength']}\n"
                                      f"\tSpeed: "
                                      f"{database[new_monster]['Speed']}\n"
                                      f"\tStealth: "
                                      f"{database[new_monster]['Stealth']}\n"
                                      f"\tCunning: "
                                      f"{database[new_monster]['Cunning']}\n"
                                      f"Please choose which of the current "
                                      f"categories you would like to change.",
                                      "Current Monster Statistics",
                                      ["Strength", "Speed", "Stealth",
                                       "Cunning", "Done"])

    while monster_stats != "Done":
        database[new_monster][monster_stats] = str(easygui.integerbox("Enter a new value for the "
                                                                      f"{monster_stats} category:\n"
                                                                      f"(must be a whole number "
                                                                      f"from 0 to 25)",
                                                                      "New Stat", 0,
                                                                      0, 25))

        # making sure the statistic value is an integer
        if database[new_monster][monster_stats] == "None":
            database[new_monster][monster_stats] = "0"

        monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                          f"current stats are:\n"
                                          f"\tStrength: "
                                          f"{database[new_monster]['Strength']}\n"
                                          f"\tSpeed: "
                                          f"{database[new_monster]['Speed']}\n"
                                          f"\tStealth: "
                                          f"{database[new_monster]['Stealth']}\n"
                                          f"\tCunning: "
                                          f"{database[new_monster]['Cunning']}\n"
                                          f"Please choose which of the current "
                                          f"categories you would like to change.",
                                          "Current Monster Statistics",
                                          ["Strength", "Speed", "Stealth",
                                           "Cunning", "Done"])

    easygui.msgbox(f"New monster card {new_monster} added to card database.",
                   "Card added", )


# function to delete a card
def delete_card(database):
    # loop to continue asking for card ID and searching database
    search_card = True

    while search_card:
        # ask user for card ID to find
        monster_ID = easygui.enterbox("Enter the name of the card you wish to delete:",
                                      "Monster Name")

        # making sure the entered ID is not an empty string or NoneType value
        if monster_ID is not None:
            if monster_ID.replace(" ", "") != "":
                # search dictionary for card ID
                for card_ID, card_stats in database.items():
                    if card_ID == monster_ID:
                        search_card = False
                        stats_lst = []
                        for stat, value in card_stats.items():
                            stats_lst.append(f"{stat} : {value}")
                        complete_stats = "\t\n".join(stats_lst)
                        delete_confirmation = easygui.buttonbox("Delete card?\n"
                                                                f"{monster_ID}\n"
                                                                f"{complete_stats}",
                                                                "Card to delete",
                                                                ["Yes", "No"])
                        # delete card if confirmed; otherwise start again
                        if delete_confirmation == "Yes":
                            del database[monster_ID]
                            easygui.msgbox(f"Monster Card '{monster_ID}' deleted.", "All Done!")
                            break
                    else:
                        search_card = True

                # ask if user wants to try again
                if search_card:
                    easygui.msgbox(f"Sorry, the card {monster_ID} could not be deleted. "
                                   f"Please check spelling, including capital letters",
                                   "Failure")
                    again = easygui.buttonbox(
                        "Would you like to enter another card name to delete?",
                        "Try again?", ["Yes", "No"])
                    if again == "No":
                        search_card = False
            else:
                easygui.msgbox("You have not entered a card to delete.", "No Name")
                search_card = False
        else:
            easygui.msgbox("Action cancelled. No card deleted.", "Cancelled")
            return


# function to find a card
def find_card(database):
    # loop to continue asking for card ID and searching database
    search_card = True

    while search_card:
        # ask user for card ID to find
        monster_ID = easygui.enterbox("Enter the name of the card you wish to find:",
                                      "Monster Name")

        # making sure the entered ID is not an empty string or NoneType value
        if monster_ID is not None:
            if monster_ID.replace(" ", "") != "":
                # search dictionary for card ID
                for card_ID, card_stats in database.items():
                    if card_ID == monster_ID:
                        search_card = False
                        stats_lst = []
                        for stat, value in card_stats.items():
                            stats_lst.append(f"{stat} : {value}")
                        complete_stats = "\t\n".join(stats_lst)
                        easygui.msgbox(f"{monster_ID}\n"
                                       f"{complete_stats}",
                                       "Card found")
                        break
                    else:
                        search_card = True

                # ask if user wants to try again
                if search_card:
                    easygui.msgbox(f"Sorry, the card {monster_ID} could not be found. "
                                   f"Please check spelling, including capital letters.",
                                   "Failure")
                    again = easygui.buttonbox(
                        "Would you like to enter another card name to find?",
                        "Try again?", ["Yes", "No"])
                    if again == "No":
                        search_card = False
            else:
                easygui.msgbox("You have not entered a card to find.", "No Name")
                search_card = True
        else:
            easygui.msgbox("Action cancelled. No card found.", "Cancelled")
            break


# function to edit a card
def edit_card(database):
    # loop to continue asking for card ID and searching database
    search_card = True

    while search_card:
        # ask user for card ID to find
        monster_ID = easygui.enterbox("Enter the name of the card you wish to edit:",
                                      "Monster Name")

        # making sure the entered ID is not an empty string or NoneType value
        if monster_ID is not None:
            if monster_ID.replace(" ", "") != "":
                # search dictionary for card ID
                for card_ID, card_stats in database.items():
                    if card_ID == monster_ID:
                        search_card = False
                        stats_lst = []
                        for stat, value in card_stats.items():
                            stats_lst.append(f"{stat} : {value}")
                        complete_stats = "\t\n".join(stats_lst)
                        easygui.msgbox(f"{monster_ID}\n"
                                       f"{complete_stats}",
                                       "Card found")
                        break
                    else:
                        search_card = True

                # ask if user wants to try again
                if search_card:
                    easygui.msgbox(f"Sorry, the card {monster_ID} could not be found. "
                                   f"Please check spelling, including capital letters.",
                                   "Failure")
                    again = easygui.buttonbox(
                        "Would you like to enter another card name to find?",
                        "Try again?", ["Yes", "No"])
                    if again == "No":
                        search_card = False
            else:
                easygui.msgbox("You have not entered a card to find and edit.", "No Name")
                search_card = True
        else:
            easygui.msgbox("Action cancelled. No card edited.", "Cancelled")
            break

        # entering stats for new card
        monster_stats = easygui.buttonbox(f"Monster card: {monster_ID}'s "
                                          f"current stats are:\n"
                                          f"\tStrength: "
                                          f"{database[monster_ID]['Strength']}\n"
                                          f"\tSpeed: "
                                          f"{database[monster_ID]['Speed']}\n"
                                          f"\tStealth: "
                                          f"{database[monster_ID]['Stealth']}\n"
                                          f"\tCunning: "
                                          f"{database[monster_ID]['Cunning']}\n"
                                          f"Please choose which of the current "
                                          f"categories you would like to change.",
                                          "Current Monster Statistics",
                                          ["Strength", "Speed", "Stealth",
                                           "Cunning", "Done"])

        while monster_stats != "Done":
            database[monster_ID][monster_stats] = str(easygui.integerbox(f"Enter a new value "
                                                                         f"for the {monster_stats} "
                                                                         f"category:\n"
                                                                         f"(must be a whole number "
                                                                         f"from 0 to 25)",
                                                                         "Change Stat",
                                                                         0, 0,
                                                                         25))

            # making sure the statistic value is an integer
            if database[monster_ID][monster_stats] == "None":
                database[monster_ID][monster_stats] = "0"

            monster_stats = easygui.buttonbox(f"Monster card: {monster_ID}'s "
                                              f"current stats are:\n"
                                              f"\tStrength: "
                                              f"{database[monster_ID]['Strength']}\n"
                                              f"\tSpeed: "
                                              f"{database[monster_ID]['Speed']}\n"
                                              f"\tStealth: "
                                              f"{database[monster_ID]['Stealth']}\n"
                                              f"\tCunning: "
                                              f"{database[monster_ID]['Cunning']}\n"
                                              f"Please choose which of the current "
                                              f"categories you would like to change.",
                                              "Current Monster Statistics",
                                              ["Strength", "Speed", "Stealth",
                                               "Cunning", "Done"])

        easygui.msgbox(f"Monster card: {monster_ID} changed.",
                       "Card changed", )


# function to print all cards
def output_all(database):
    # loop to output all the cards in the database, one by one
    for card_ID, card_stats in database.items():
        stats_lst = []
        for stat, value in card_stats.items():
            stats_lst.append(f"{stat} : {value}")
        complete_stats = "\n\t".join(stats_lst)
        card_formatter(f"Monster card: {card_ID}\n\t"
                       f"{complete_stats}")
    easygui.msgbox("Note: see Python Console for cards printed out.", "Output Location",
                   "Got it!")


# function to format outputted cards
def card_formatter(card):
    # finds the different stats and adds emojis to the card
    index = card.find("Strength")
    emoji_card = card[:index] + "💪" + card[index:]
    index = emoji_card.find("Speed")
    emoji_card = emoji_card[:index] + "🏃" + emoji_card[index:]
    index = emoji_card.find("Stealth")
    emoji_card = emoji_card[:index] + "🥷" + emoji_card[index:]
    index = card.find("Cunning")
    emoji_card = emoji_card[:(index + 3)] + "🧠" + emoji_card[(index + 3):]
    print("~" * 25)
    print(emoji_card)
    print("~" * 25)


# Main routine goes here:
# setting up initial card database
card_dict = {
    "Stoneling": {
        "Strength": "7",
        "Speed": "1",
        "Stealth": "25",
        "Cunning": "15"
    },
    "Vexscream": {
        "Strength": "1",
        "Speed": "6",
        "Stealth": "21",
        "Cunning": "19"
    },
    "Dawnmirage": {
        "Strength": "5",
        "Speed": "15",
        "Stealth": "18",
        "Cunning": "22"
    },
    "Blazegolem": {
        "Strength": "15",
        "Speed": "20",
        "Stealth": "23",
        "Cunning": "6"
    },
    "Websnake": {
        "Strength": "7",
        "Speed": "15",
        "Stealth": "10",
        "Cunning": "5"
    },
    "Moldvine": {
        "Strength": "21",
        "Speed": "18",
        "Stealth": "14",
        "Cunning": "5"
    },
    "Vortexwing": {
        "Strength": "19",
        "Speed": "13",
        "Stealth": "19",
        "Cunning": "2"
    },
    "Rotthing": {
        "Strength": "16",
        "Speed": "7",
        "Stealth": "4",
        "Cunning": "12"
    },
    "Froststep": {
        "Strength": "14",
        "Speed": "14",
        "Stealth": "17",
        "Cunning": "4"
    },
    "Wispghoul": {
        "Strength": "17",
        "Speed": "19",
        "Stealth": "3",
        "Cunning": "2"
    },
}

# welcome the user
welcome_instructions("Monster Cards",
                     ["Choose an action after this box",
                      "To add a card: enter a card name, then fill in the "
                      "stats for the card, then confirm your entry.",
                      "To delete a card, enter the card name and confirm your "
                      "choice.",
                      "To find a card, enter the specific card name.",
                      "'Output all' allows you to see which cards are already "
                      "present in the menu.",
                      "Once you have finished, exit the program."])

# start main program with action screen
action_screen(card_dict)
