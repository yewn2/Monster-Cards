"""
Component 2 (Action choices) v2
Places version 1 into a function for easier use in future
Adds calls for choice functions (commented out for now)
Copied from previous project: Burger Menu Combos
"""


# imports
import easygui


def action_screen(cards):
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "MONSTER CARDS",
                               ["Add card", "Delete card",
                                "Find card", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # # check the choice and call the appropriate function
        # if choice == "Add card":
        #     add_card(cards)
        # elif choice == "Delete card":
        #     del_card(cards)
        # elif choice == "Find card":
        #     find_card(cards)
        # elif choice == "Output all":
        #     print_all(cards)

        # display action screen with choices again
        choice = easygui.buttonbox("What would you like to do?",
                                   "MONSTER CARD DATABASE EDITOR",
                                   ["Add card", "Delete card",
                                    "Find card", "Output all", "Exit"])

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Monster Cards",
                   "Goodbye!")


# main program
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
action_screen(card_dict)
