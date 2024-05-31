"""
Find card version 1
This component is essentially the 'delete_card' component but without the deleting part.
Easygui has been added for this version, but code has not been placed into a function.
"""

# imports
import easygui

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
            for card_ID, card_stats in card_dict.items():
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
                easygui.msgbox(f"Sorry, the card {monster_ID} could not be found.", "Failure")
                again = easygui.buttonbox(
                    "Would you like to enter another card name to find?",
                    "Try again?", ["Yes", "No"])
                if again == "No":
                    search_card = True
        else:
            easygui.msgbox("You have not entered a card to find.", "No Name")
            search_card = False
    else:
        easygui.msgbox("Action cancelled. No card found.", "Cancelled")
        break
