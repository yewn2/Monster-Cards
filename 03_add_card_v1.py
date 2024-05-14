"""
Add card version 1
Preliminary code, not placed in a function.
Trialling Add card with a dictionary format.
Easygui added to see effects on output.
Asks user to enter card name and fill in stats categories before confirming.
"""

# imports
import easygui

# setting up initial card list
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

# ask user for card name
new_monster = easygui.enterbox("Enter a name for your new monster card:",
                               "New Monster")

# name confirmation
confirm_monster = easygui.buttonbox(f"The name you want to have for your new "
                                    f"card is {new_monster}.",
                                    "Monster Name Confirmation",
                                    ["Yes", "No"])

while confirm_monster != "Yes":
    # ask user for card name again
    new_monster = easygui.enterbox("Enter a name for your new monster card:",
                                   "New Monster")
    # name confirmation again
    confirm_monster = easygui.buttonbox(
        f"The name you want to have for your new "
        f"card is {new_monster}.",
        "Monster Name Confirmation",
        ["Yes", "No"])

# add card name to card database; set stat categories by default  to 0
card_dict[new_monster] = {}
card_dict[new_monster]["Strength"] = "0"
card_dict[new_monster]["Speed"] = "0"
card_dict[new_monster]["Stealth"] = "0"
card_dict[new_monster]["Cunning"] = "0"

# entering stats for new card
monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                  f"current stats are:\n"
                                  f"\tStrength: "
                                  f"{card_dict[new_monster]['Strength']}\n"
                                  f"\tSpeed: "
                                  f"{card_dict[new_monster]['Speed']}\n"
                                  f"\tStealth: "
                                  f"{card_dict[new_monster]['Stealth']}\n"
                                  f"\tCunning: "
                                  f"{card_dict[new_monster]['Cunning']}\n"
                                  f"Please choose which of the current "
                                  f"categories you would like to change.",
                                  "Current Monster Statistics",
                                  ["Strength", "Speed", "Stealth",
                                   "Cunning", "I don't want "
                                              "to change anything"])

while monster_stats != "I don't want to change anything":
    card_dict[new_monster][monster_stats] = str(easygui.integerbox("Enter a new value for the "
                                                                   f"{monster_stats} category: \n"
                                                                   f"(must be a whole number "
                                                                   f"between 0 and 25)",
                                                                   "New Stat", 0,
                                                                   0, 25))

    # making sure the statistic value is an integer
    if card_dict[new_monster][monster_stats] == "None":
        card_dict[new_monster][monster_stats] = "0"

    monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                      f"current stats are:\n"
                                      f"\tStrength: "
                                      f"{card_dict[new_monster]['Strength']}\n"
                                      f"\tSpeed: "
                                      f"{card_dict[new_monster]['Speed']}\n"
                                      f"\tStealth: "
                                      f"{card_dict[new_monster]['Stealth']}\n"
                                      f"\tCunning: "
                                      f"{card_dict[new_monster]['Cunning']}\n"
                                      f"Please choose which of the current "
                                      f"categories you would like to change.",
                                      "Current Monster Statistics",
                                      ["Strength", "Speed", "Stealth",
                                       "Cunning", "I don't want "
                                                  "to change anything"])

print(card_dict)
