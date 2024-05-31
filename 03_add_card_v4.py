"""
Add card version 4
After testing by an outside individual (my father), I am now improving my component based on his
suggestions.
"""

# imports
import easygui


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

    while monster_stats != "I don't want to change anything":
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
                                           "Cunning", "I don't want "
                                                      "to change anything"])


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

# main program
add_card(card_dict)
